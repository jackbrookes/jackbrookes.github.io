from codecs import encode
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
    def __init__(self, template_path, content_dir, data):
        """
        Instantiate a new buildable website.
        """

        self.template_path = template_path
        self.content_dir = content_dir
        self.data = data

    def build(self, output_dir):
        """
        Begin the build process, and converting all content/*.md
        files into pages. 
        """

        mds = glob.glob(os.path.join(self.content_dir, "**", "*.md"), recursive=True)
        for md in mds:
            is_index = md == os.path.join(self.content_dir, "index.md")
            self.build_html_from_md(md, output_dir, is_index=is_index)


    def build_html_from_md(self, md_path, output_dir, is_index=False):
        """
        Build HTML page from markdown path. Creates a directory and index.html page.
        """

        with open(self.template_path, encoding="utf-8") as template_file:
            html_content = markdown2.markdown_path(
                md_path,
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
            os.makedirs(os.path.dirname(newpath), exist_ok=True)
            with open(newpath, "w+", encoding="utf-8") as newf:
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
        replacement = eval(match.group(1), {**kwargs, **globals()})
        s, e = match.span()
        chars[s:e] = replacement
    return ''.join(chars)

def write_meta_date(metadata):
    if "date" in metadata:
        return f'<meta property="article:published_time" content={metadata["date"]} />'
    else:
        return ''

def write_post_date(metadata):
    if "date" in metadata:
        return f'<p class="date">Published {metadata["date"]}</p>'
    else:
      return ''

def generate_post_row(metadata, name):
    """
    Generates a table row for a given metadata.
    """
    return f'''
    <tr>
        <td><a href="{name}">{metadata["title"]}<a></td>
        <td>{metadata["date"]}</td>
    </tr>
    '''

if __name__ == "__main__":
    # use script directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    data = yaml.load(open("constants.yaml"))
    post_files = glob.glob(os.path.join("content/posts/", "**", "*.md"), recursive=True)
    post_files = [f for f in post_files if os.path.split(f)[1] != "test.md"]
    post_metadata = (markdown2.markdown_path(x, extras=["metadata"]).metadata for x in post_files)
    post_names = (os.path.split(os.path.relpath(x))[1].replace('.md', '') for x in post_files)
    posts = sorted(zip(post_metadata, post_names), key=lambda v: v[0]["date"], reverse=True)
    post_rows = (generate_post_row(meta, name) for meta, name in posts)

    data["posts_list"] = post_rows
    data["current_year"] = str(datetime.datetime.now().year)

    builder = Builder(
        template_path="template.html",
        content_dir="content",
        data=data
    )

    # output in parent directory
    builder.build("..")