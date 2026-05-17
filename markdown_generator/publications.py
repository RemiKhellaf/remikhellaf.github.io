import pandas as pd
import os

# Import TSV
# Note: Ensure your TSV now includes 'status' and 'slides_url' columns.
publications = pd.read_csv("publications.tsv", sep="\t", header=0)

# Fill empty values with an empty string so they don't print as 'nan'
publications = publications.fillna("")

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
}

def html_escape(text):
    """Produce entities within text."""
    return "".join(html_escape_table.get(c, c) for c in str(text))

for row, item in publications.iterrows():
    md_filename = str(item.pub_date) + "-" + str(item.url_slug) + ".md"
    html_filename = str(item.pub_date) + "-" + str(item.url_slug)
    
    # 1. Clean Variables
    title = item.title
    excerpt = html_escape(item.excerpt)
    venue = html_escape(item.venue)
    citation = html_escape(item.citation)
    
    # Use .get() to avoid crashing if columns are accidentally missing
    paper_url = str(item.get('paper_url', '')).strip()
    slides_url = str(item.get('slides_url', '')).strip()
    status = str(item.get('status', 'Accepted')).strip() # Defaults to Accepted
    
    # 2. Build Minimalist YAML Frontmatter
    md  = "---\n"
    md += f"title: \"{title}\"\n"
    md += "collection: publications\n"
    md += f"type: '{status}'\n" # This lets you group Preprints vs Accepted in Jekyll
    md += f"permalink: /publication/{html_filename}\n"
    
    if excerpt:
        md += f"excerpt: '{excerpt}'\n"
        
    md += f"date: {item.pub_date}\n"
    
    if venue:
        md += f"venue: '{venue}'\n"
        
    # Commented out URLs in the YAML per your requested format
    if slides_url:
        md += f"# slidesurl: '{slides_url}'\n"
        
    if paper_url:
        md += f"# paperurl: '{paper_url}'\n"
        
    md += f"citation: '{citation}'\n"
    md += "---\n\n"
    
    # 3. Build Minimalist Markdown Body
    if paper_url:
        md += f"[Download paper here]({paper_url})\n\n"
        
    if slides_url:
        md += f"[Download slides here]({slides_url})\n\n"
        
    # HTML commented citation per your requested format
    md += f"<!-- Recommended citation: {citation} -->\n"
    
    # 4. Save File
    md_filename = os.path.basename(md_filename)
    save_path = "../_publications/"
    
    # Ensure the directory exists
    os.makedirs(save_path, exist_ok=True)
    
    with open(os.path.join(save_path, md_filename), 'w') as f:
        f.write(md)