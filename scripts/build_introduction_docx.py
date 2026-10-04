"""
Build publication-ready DOCX for Introduction (Mở đầu) of Capstone Project.
Adheres strictly to HUIT 2024 Institutional Profile and project decisions.
"""

import os
import re
from docx import Document
from docx.shared import Inches, Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

def add_footer_page_number(run):
    """Inserts a dynamic PAGE field into a Word run."""
    fldChar1 = parse_xml(r'<w:fldChar %s w:fldCharType="begin"/>' % nsdecls('w'))
    instrText = parse_xml(r'<w:instrText %s xml:space="preserve"> PAGE </w:instrText>' % nsdecls('w'))
    fldChar2 = parse_xml(r'<w:fldChar %s w:fldCharType="separate"/>' % nsdecls('w'))
    t = parse_xml(r'<w:t %s>1</w:t>' % nsdecls('w'))
    fldChar3 = parse_xml(r'<w:fldChar %s w:fldCharType="end"/>' % nsdecls('w'))
    run._r.append(fldChar1)
    run._r.append(instrText)
    run._r.append(fldChar2)
    run._r.append(t)
    run._r.append(fldChar3)

def clear_paragraph_borders(paragraph):
    """Removes all borders from a paragraph (prevents default Word title horizontal rules)."""
    pPr = paragraph._p.get_or_add_pPr()
    for child in list(pPr):
        if child.tag.endswith('pBdr'):
            pPr.remove(child)
    pBdr = parse_xml(
        r'<w:pBdr %s>'
        r'<w:top w:val="none" w:sz="0" w:space="0" w:color="auto"/>'
        r'<w:left w:val="none" w:sz="0" w:space="0" w:color="auto"/>'
        r'<w:bottom w:val="none" w:sz="0" w:space="0" w:color="auto"/>'
        r'<w:right w:val="none" w:sz="0" w:space="0" w:color="auto"/>'
        r'</w:pBdr>' % nsdecls('w')
    )
    pPr.append(pBdr)

def setup_huit_document():
    doc = Document()
    
    # Page setup: A4, Margins: Top 3.5cm, Bottom 3.0cm, Left 3.5cm, Right 2.0cm
    section = doc.sections[0]
    section.page_width = Cm(21.0)
    section.page_height = Cm(29.7)
    section.top_margin = Cm(3.5)
    section.bottom_margin = Cm(3.0)
    section.left_margin = Cm(3.5)
    section.right_margin = Cm(2.0)
    
    # Configure styles
    styles = doc.styles
    
    # Normal Style
    normal = styles['Normal']
    normal.font.name = 'Times New Roman'
    normal.font.size = Pt(13)
    normal.font.color.rgb = RGBColor(0, 0, 0)
    normal.paragraph_format.line_spacing = 1.5
    normal.paragraph_format.space_before = Pt(0)
    normal.paragraph_format.space_after = Pt(6)
    normal.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    
    # Heading 1 Style
    h1 = styles['Heading 1']
    h1.font.name = 'Times New Roman'
    h1.font.size = Pt(14)
    h1.font.bold = True
    h1.font.color.rgb = RGBColor(0, 0, 0)
    h1.paragraph_format.line_spacing = 1.5
    h1.paragraph_format.space_before = Pt(14)
    h1.paragraph_format.space_after = Pt(6)
    h1.paragraph_format.keep_with_next = True
    h1.paragraph_format.first_line_indent = Pt(0)
    h1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    
    # Heading 2 Style
    h2 = styles['Heading 2']
    h2.font.name = 'Times New Roman'
    h2.font.size = Pt(13)
    h2.font.bold = True
    h2.font.color.rgb = RGBColor(0, 0, 0)
    h2.paragraph_format.line_spacing = 1.5
    h2.paragraph_format.space_before = Pt(10)
    h2.paragraph_format.space_after = Pt(4)
    h2.paragraph_format.keep_with_next = True
    h2.paragraph_format.first_line_indent = Pt(0)
    h2.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    
    # Title Style
    try:
        title_style = styles['Title']
    except KeyError:
        title_style = styles.add_style('Title', WD_STYLE_TYPE.PARAGRAPH)
    title_style.font.name = 'Times New Roman'
    title_style.font.size = Pt(18)
    title_style.font.bold = True
    title_style.font.color.rgb = RGBColor(0, 0, 0)
    title_style.paragraph_format.line_spacing = 1.5
    title_style.paragraph_format.space_before = Pt(12)
    title_style.paragraph_format.space_after = Pt(18)
    title_style.paragraph_format.keep_with_next = True
    title_style.paragraph_format.first_line_indent = Pt(0)
    title_style.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    # Clear borders on title_style
    pPr = title_style._element.get_or_add_pPr()
    for child in list(pPr):
        if child.tag.endswith('pBdr'):
            pPr.remove(child)

    # Setup footer for page numbering
    section.footer_distance = Cm(1.5)
    footer = section.footer
    footer.is_linked_to_previous = False
    fp = footer.paragraphs[0]
    fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    fp.text = ""
    frun = fp.add_run()
    frun.font.name = "Times New Roman"
    frun.font.size = Pt(10)
    frun.font.color.rgb = RGBColor(0, 0, 0)
    add_footer_page_number(frun)
    
    return doc

def format_inline_runs(paragraph, text):
    """
    Parses markdown inline bold (**text**), italic (*text*), and code (`text`).
    Adds runs to the given paragraph with appropriate styling.
    """
    pattern = re.compile(r'(\*\*.*?\*\*|\*.*?\*|`.*?`)')
    parts = pattern.split(text)
    
    for part in parts:
        if not part:
            continue
        if part.startswith('**') and part.endswith('**') and len(part) >= 4:
            run = paragraph.add_run(part[2:-2])
            run.font.name = 'Times New Roman'
            run.font.size = Pt(13)
            run.font.bold = True
            run.font.color.rgb = RGBColor(0, 0, 0)
        elif part.startswith('*') and part.endswith('*') and len(part) >= 2:
            run = paragraph.add_run(part[1:-1])
            run.font.name = 'Times New Roman'
            run.font.size = Pt(13)
            run.font.italic = True
            run.font.color.rgb = RGBColor(0, 0, 0)
        elif part.startswith('`') and part.endswith('`') and len(part) >= 2:
            # Inline code formatted in Times New Roman italic for academic elegance
            run = paragraph.add_run(part[1:-1])
            run.font.name = 'Times New Roman'
            run.font.size = Pt(13)
            run.font.italic = True
            run.font.color.rgb = RGBColor(0, 0, 0)
        else:
            run = paragraph.add_run(part)
            run.font.name = 'Times New Roman'
            run.font.size = Pt(13)
            run.font.color.rgb = RGBColor(0, 0, 0)

def build_docx_from_markdown(md_path, docx_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    doc = setup_huit_document()
    
    in_references = False
    
    i = 0
    n = len(lines)
    while i < n:
        raw_line = lines[i].strip()
        
        # Blank line or horizontal rule
        if not raw_line or raw_line == '---':
            i += 1
            continue
            
        # Top-level Title: # MỞ ĐẦU
        if raw_line.startswith('# '):
            title_text = raw_line[2:].strip()
            p = doc.add_paragraph(title_text, style='Title')
            clear_paragraph_borders(p)
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.keep_with_next = True
            p.paragraph_format.space_before = Pt(12)
            p.paragraph_format.space_after = Pt(18)
            i += 1
            continue
            
        # Level 1 Heading: ## 1. ... or ## TÀI LIỆU THAM KHẢO
        if raw_line.startswith('## '):
            h1_text = raw_line[3:].strip()
            if 'TÀI LIỆU THAM KHẢO' in h1_text.upper():
                in_references = True
                # Start References on a fresh page for clean thesis structure
                p = doc.add_paragraph(h1_text, style='Heading 1')
                p.paragraph_format.page_break_before = True
            else:
                p = doc.add_paragraph(h1_text, style='Heading 1')
            
            clear_paragraph_borders(p)
            p.paragraph_format.keep_with_next = True
            p.paragraph_format.space_before = Pt(14)
            p.paragraph_format.space_after = Pt(6)
            i += 1
            continue
            
        # Level 2 Heading: ### 2.1. ...
        if raw_line.startswith('### '):
            h2_text = raw_line[4:].strip()
            p = doc.add_paragraph(h2_text, style='Heading 2')
            clear_paragraph_borders(p)
            p.paragraph_format.keep_with_next = True
            p.paragraph_format.space_before = Pt(10)
            p.paragraph_format.space_after = Pt(4)
            i += 1
            continue
            
        # Reference Item: [1] ...
        if in_references and raw_line.startswith('['):
            p = doc.add_paragraph(style='Normal')
            p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            p.paragraph_format.left_indent = Cm(1.0)
            p.paragraph_format.first_line_indent = Cm(-1.0) # Hanging indent
            p.paragraph_format.line_spacing = 1.5
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(6)
            p.paragraph_format.keep_together = True # Prevent splitting entry across pages
            format_inline_runs(p, raw_line)
            i += 1
            continue
            
        # Numbered List Item: e.g. 1. **Mục tiêu 1 (O1):** ...
        m_num = re.match(r'^(\d+)\.\s+(.*)$', raw_line)
        if m_num and not in_references:
            p = doc.add_paragraph(style='Normal')
            p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            p.paragraph_format.left_indent = Cm(1.25)
            p.paragraph_format.first_line_indent = Cm(-0.63) # Hanging indent
            p.paragraph_format.line_spacing = 1.5
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(4)
            p.paragraph_format.keep_together = True
            
            num_str = m_num.group(1) + ". "
            content_str = m_num.group(2)
            
            # Add number run
            r_num = p.add_run(num_str)
            r_num.font.name = 'Times New Roman'
            r_num.font.size = Pt(13)
            r_num.font.bold = True
            r_num.font.color.rgb = RGBColor(0, 0, 0)
            
            format_inline_runs(p, content_str)
            i += 1
            continue
            
        # Bullet List Item: e.g. - **Phạm vi...:** ... or - Giao thức...
        if raw_line.startswith('- ') or raw_line.startswith('* '):
            content_str = raw_line[2:].strip()
            p = doc.add_paragraph(style='Normal')
            p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            p.paragraph_format.left_indent = Cm(1.25)
            p.paragraph_format.first_line_indent = Cm(-0.63) # Hanging indent
            p.paragraph_format.line_spacing = 1.5
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(4)
            p.paragraph_format.keep_together = True
            
            # Bullet symbol
            r_bullet = p.add_run("•  ")
            r_bullet.font.name = 'Times New Roman'
            r_bullet.font.size = Pt(13)
            r_bullet.font.color.rgb = RGBColor(0, 0, 0)
            
            format_inline_runs(p, content_str)
            i += 1
            continue
            
        # Regular Body Paragraph
        p = doc.add_paragraph(style='Normal')
        p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.first_line_indent = Cm(1.25) # Standard HUIT first line indent
        p.paragraph_format.left_indent = Pt(0)
        p.paragraph_format.line_spacing = 1.5
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(6)
        
        # If this paragraph is a short introductory lead-in ending with ':', keep with next
        if raw_line.endswith(':') and len(raw_line) < 150:
            p.paragraph_format.keep_with_next = True
            
        format_inline_runs(p, raw_line)
        i += 1

    # Save document
    os.makedirs(os.path.dirname(docx_path), exist_ok=True)
    doc.save(docx_path)
    print(f"Successfully generated DOCX at: {docx_path}")

if __name__ == '__main__':
    md_file = 'work/do-an/INTRODUCTION.md'
    out_file = 'work/do-an/outputs/MO_DAU_DO_AN.docx'
    build_docx_from_markdown(md_file, out_file)
