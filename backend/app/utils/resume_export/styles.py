"""
==================================================
Resume Typography & Styles
Career AI Intelligence Platform
Microsoft Resume Theme
==================================================
"""

from docx.shared import Pt
from docx.shared import RGBColor

from docx.enum.text import (
    WD_PARAGRAPH_ALIGNMENT
)

from .constants import *


class ResumeStyle:

    # ==================================================
    # Candidate Name
    # ==================================================

    @staticmethod
    def name(run):

        run.font.name = FONT_NAME
        run.font.size = Pt(NAME_FONT_SIZE)
        run.font.bold = True
        run.font.color.rgb = RGBColor.from_string(
            TEXT_COLOR
        )

    # ==================================================
    # Professional Role
    # ==================================================

    @staticmethod
    def title(run):

        run.font.name = TITLE_FONT
        run.font.size = Pt(TITLE_FONT_SIZE)
        run.font.bold = False
        run.font.italic = False

        run.font.color.rgb = RGBColor.from_string(
            HEADER_COLOR
        )

    # ==================================================
    # Section Heading
    # ==================================================

    @staticmethod
    def section(run):

        run.font.name = FONT_NAME

        run.font.size = Pt(
            SECTION_FONT_SIZE
        )

        run.font.bold = True

        run.font.color.rgb = RGBColor.from_string(
            HEADER_COLOR
        )

    # ==================================================
    # Normal Body
    # ==================================================

    @staticmethod
    def body(run):

        run.font.name = BODY_FONT

        run.font.size = Pt(
            BODY_FONT_SIZE
        )

        run.font.bold = False

        run.font.color.rgb = RGBColor.from_string(
            TEXT_COLOR
        )

    # ==================================================
    # Small Text
    # ==================================================

    @staticmethod
    def small(run):

        run.font.name = BODY_FONT

        run.font.size = Pt(
            SMALL_FONT_SIZE
        )

        run.font.bold = False

        run.font.color.rgb = RGBColor.from_string(
            TEXT_COLOR
        )

    # ==================================================
    # Bold Body
    # ==================================================

    @staticmethod
    def bold(run):

        ResumeStyle.body(run)

        run.font.bold = True

    # ==================================================
    # Hyperlink
    # ==================================================

    @staticmethod
    def hyperlink(run):

        run.font.name = BODY_FONT

        run.font.size = Pt(
            BODY_FONT_SIZE
        )

        run.font.bold = False

        run.font.underline = True

        run.font.color.rgb = RGBColor.from_string(
            LINK_COLOR
        )

    # ==================================================
    # Center Alignment
    # ==================================================

    @staticmethod
    def center(paragraph):

        paragraph.alignment = (
            WD_PARAGRAPH_ALIGNMENT.CENTER
        )

    # ==================================================
    # Left Alignment
    # ==================================================

    @staticmethod
    def left(paragraph):

        paragraph.alignment = (
            WD_PARAGRAPH_ALIGNMENT.LEFT
        )

    # ==================================================
    # Right Alignment
    # ==================================================

    @staticmethod
    def right(paragraph):

        paragraph.alignment = (
            WD_PARAGRAPH_ALIGNMENT.RIGHT
        )

    # ==================================================
    # Justify
    # ==================================================

    @staticmethod
    def justify(paragraph):

        paragraph.alignment = (
            WD_PARAGRAPH_ALIGNMENT.JUSTIFY
        )

    # ==================================================
    # Paragraph Spacing
    # ==================================================

    @staticmethod
    def paragraph_spacing(

        paragraph,

        before=0,

        after=6,

        line=1.15

    ):

        fmt = paragraph.paragraph_format

        fmt.space_before = Pt(before)

        fmt.space_after = Pt(after)

        fmt.line_spacing = line

    # ==================================================
    # Resume Header
    # ==================================================

    @staticmethod
    def header(paragraph):

        ResumeStyle.center(paragraph)

        ResumeStyle.paragraph_spacing(

            paragraph,

            before=0,

            after=2

        )

    # ==================================================
    # Section Header
    # ==================================================

    @staticmethod
    def section_header(paragraph):

        ResumeStyle.left(paragraph)

        ResumeStyle.paragraph_spacing(

            paragraph,

            before=12,

            after=6

        )

    # ==================================================
    # Bullet Item
    # ==================================================

    @staticmethod
    def bullet(paragraph):

        ResumeStyle.left(paragraph)

        ResumeStyle.paragraph_spacing(

            paragraph,

            before=0,

            after=1

        )

    # ==================================================
    # Compact Paragraph
    # ==================================================

    @staticmethod
    def compact(paragraph):

        ResumeStyle.left(paragraph)

        ResumeStyle.paragraph_spacing(

            paragraph,

            before=0,

            after=2

        )