from datetime import datetime
from pathlib import Path
import xml.etree.ElementTree as ET

urlset = ET.Element(
    "urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
)
base_url = "https://what-is-calculus.xyz"  # Change to your domain

for f in Path(".").glob("*.html"):
  url = ET.SubElement(urlset, "url")
  loc = f"{base_url}/" if f.name == "index.html" else f"{base_url}/{f.name}"
  ET.SubElement(url, "loc").text = loc
  ET.SubElement(url, "lastmod").text = datetime.fromtimestamp(
      f.stat().st_mtime
  ).strftime("%Y-%m-%d")

tree = ET.ElementTree(urlset)
ET.indent(tree)
tree.write("sitemap.xml", encoding="utf-8", xml_declaration=True)