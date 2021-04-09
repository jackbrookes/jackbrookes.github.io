import markdown2
import yaml
import re
import os
from distutils.dir_util import copy_tree
import glob
import datetime

class Builder(object):
    """
    Represents an buildable website.
    """
    def __init__(self, template_path, content_dir, static_dir, data):
        """
        Instantiate a new buildable website.
        """

        self.template_path = template_path
        self.content_dir = content_dir
        self.static_dir = static_dir
        self.data = data
        
    def copy_static_files(self, output_dir):
        """
        Copy files from static directory to output static directory.
        """

        src = self.static_dir
        dst = os.path.join(output_dir, self.static_dir)
        copy_tree(src, dst)

    def build(self, output_dir):
        """
        Begin the build process, copying static files, and converting all content/*.md
        files into pages. 
        """

        self.copy_static_files(output_dir)
        mds = glob.glob(os.path.join(self.content_dir, "**", "*.md"), recursive=True)
        for md in mds:
            is_index = md == os.path.join(self.content_dir, "index.md")
            self.build_html_from_md(md, output_dir, is_index=is_index)


    def build_html_from_md(self, md_path, output_dir, is_index=False):
        """
        Build HTML page from markdown path. Creates a directory and index.html page.
        """

        with open(self.template_path) as template_file:
            with open(md_path) as md_file:
                html_content = markdown2.markdown(
                    md_file.read(),
                    extras=["metadata", "fenced-code-blocks", "codehilite", "header-ids"]
                )
                replaced_html_content = replace_template(
                    html_content,
                    data=self.data,
                    metadata=html_content.metadata
                )
                replaced_text = replace_template(
                    template_file.read(),
                    data=self.data,
                    content=replaced_html_content,
                    metadata=html_content.metadata
                )
                (parent, fname) = os.path.split(os.path.relpath(md_path))
                fname_pure = fname.replace(".md", "")

                if is_index:
                    newpath = os.path.join(
                        output_dir,
                        "index.html"
                    )
                else:
                    newpath = os.path.join(
                        output_dir,
                        os.path.relpath(parent, start=self.content_dir),
                        fname_pure,
                        "index.html"
                    )
                
                os.makedirs(os.path.dirname(newpath), exist_ok=True)
                with open(newpath, "w+") as newf:
                    newf.write(replaced_text)
                    
def replace_template(text, **kwargs):
    """
    Replaces template strings within a template with specified content. Template
    strings use double curly brackets, and evaluates the contents. 
    e.g. {{ print("hello") }}.
    Anything in **kwargs are available for evaluation.
    """
    matches = re.finditer(r"\{\{(.*?)\}\}", text)
    chars = list(text)
    for match in reversed(list(matches)):
        replacement = eval(match.group(1), kwargs)
        s, e = match.span()
        chars[s:e] = replacement
    return ''.join(chars)


if __name__ == "__main__":
    data = yaml.load(open("constants.yaml"))
    post_files = glob.glob(os.path.join("content/posts/", "**", "*.md"), recursive=True)
    post_titles = (markdown2.markdown(open(x).read(), extras=["metadata"]).metadata["title"] for x in post_files)
    post_names = (os.path.split(os.path.relpath(x))[1].replace('.md', '') for x in post_files)
    post_mds = (f"* [{title}]({name})" for title, name in zip(post_titles, post_names))

    data["posts_list"] = markdown2.markdown('\n'.join(post_mds))
    data["current_year"] = str(datetime.datetime.now().year)

    builder = Builder(
        template_path="template.html",
        content_dir="content",
        static_dir="static",
        data=data
    )

    # output in parent directory
    builder.build("..")