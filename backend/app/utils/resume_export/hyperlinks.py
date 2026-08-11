"""
==================================================
Resume Hyperlink Utilities
Career AI Intelligence Platform
==================================================
"""

from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.opc.constants import RELATIONSHIP_TYPE

from .constants import LINK_COLOR


class ResumeHyperlink:

    # ==================================================
    # Normalize URL
    # ==================================================

    @staticmethod
    def normalize_url(url: str) -> str:

        if not url:
            return ""

        url = str(url).strip()

        if not url:
            return ""

        # Already has a valid scheme
        if url.startswith(
            (
                "http://",
                "https://",
                "mailto:",
                "tel:"
            )
        ):
            return url

        # LinkedIn
        if "linkedin.com" in url.lower():

            if not url.startswith("www."):

                return f"https://{url}"

            return f"https://{url}"

        # GitHub
        if "github.com" in url.lower():

            if not url.startswith("www."):

                return f"https://{url}"

            return f"https://{url}"

        # Generic website
        return f"https://{url}"

    # ==================================================
    # Add Clickable Hyperlink
    # ==================================================

    @staticmethod
    def add(
        paragraph,
        text: str,
        url: str
    ):

        if not text or not url:
            return

        url = ResumeHyperlink.normalize_url(url)

        if not url:
            return

        part = paragraph.part

        relationship_id = part.relate_to(
            url,
            RELATIONSHIP_TYPE.HYPERLINK,
            is_external=True
        )

        hyperlink = OxmlElement(
            "w:hyperlink"
        )

        hyperlink.set(
            qn("r:id"),
            relationship_id
        )

        run = OxmlElement("w:r")

        properties = OxmlElement("w:rPr")

        # ------------------------------------------
        # Font Color
        # ------------------------------------------

        color = OxmlElement("w:color")

        color.set(
            qn("w:val"),
            LINK_COLOR
        )

        properties.append(color)

        # ------------------------------------------
        # Underline
        # ------------------------------------------

        underline = OxmlElement("w:u")

        underline.set(
            qn("w:val"),
            "single"
        )

        properties.append(underline)

        # ------------------------------------------
        # Font
        # ------------------------------------------

        rfonts = OxmlElement("w:rFonts")

        rfonts.set(
            qn("w:ascii"),
            "Calibri"
        )

        rfonts.set(
            qn("w:hAnsi"),
            "Calibri"
        )

        properties.append(rfonts)

        run.append(properties)

        # ------------------------------------------
        # Hyperlink Text
        # ------------------------------------------

        text_element = OxmlElement("w:t")

        text_element.text = text

        run.append(text_element)

        hyperlink.append(run)

        paragraph._p.append(
            hyperlink
        )

    # ==================================================
    # Email
    # ==================================================

    @staticmethod
    def email(
        paragraph,
        email: str
    ):

        if not email:
            return

        ResumeHyperlink.add(
            paragraph,
            email,
            f"mailto:{email}"
        )

    # ==================================================
    # Phone
    # ==================================================

    @staticmethod
    def phone(
        paragraph,
        phone: str
    ):

        if not phone:
            return

        ResumeHyperlink.add(
            paragraph,
            phone,
            f"tel:{phone}"
        )

    # ==================================================
    # LinkedIn
    # ==================================================

    @staticmethod
    def linkedin(
        paragraph,
        url: str
    ):

        if not url:
            return

        ResumeHyperlink.add(
            paragraph,
            "LinkedIn",
            url
        )

    # ==================================================
    # GitHub
    # ==================================================

    @staticmethod
    def github(
        paragraph,
        url: str
    ):

        if not url:
            return

        ResumeHyperlink.add(
            paragraph,
            "GitHub",
            url
        )

    # ==================================================
    # Portfolio
    # ==================================================

    @staticmethod
    def portfolio(
        paragraph,
        url: str
    ):

        if not url:
            return

        ResumeHyperlink.add(
            paragraph,
            "Portfolio",
            url
        )