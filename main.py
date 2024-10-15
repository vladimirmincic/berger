from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from rounds import get_rounds_data
from datetime import datetime

rounds = 14
tournament_name = "Tournament"


class BergerTournamentPDF:
    def __init__(self, rounds, tournament):
        self.rounds = rounds
        self.tournament = tournament
        self.filename = self.generate_filename()

    def generate_filename(self):
        # Format the current date
        current_date = datetime.now().strftime("%d-%m-%Y")
        # Generate the PDF filename
        return f"berger_{self.rounds}_{self.tournament}_{current_date}.pdf"

    def create_pdf(self):
        custom_page_size = (1500, 500)

        # Create a PDF document with custom page size
        doc = SimpleDocTemplate(self.filename, pagesize=custom_page_size)

        # Get table data from rounds.py
        table_data = get_rounds_data(self.rounds)

        # Create styles for the paragraph
        styles = getSampleStyleSheet()
        title_style = styles['Title']

        # Create the tournament title as a Paragraph
        tournament_title = Paragraph(self.tournament, title_style)

        # Create the table
        table = Table(table_data)

        # Apply styles to the table
        style = TableStyle([('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                            ('BACKGROUND', (0, 0), (-1, 0), (0.9, 0.9, 0.9)),
                            ('GRID', (0, 0), (-1, -1), 1, (0, 0, 0))])

        table.setStyle(style)

        # Build the PDF document with the title and table
        elements = [tournament_title, table]
        doc.build(elements)


if __name__ == "__main__":
    tournament_pdf = BergerTournamentPDF(rounds, tournament_name)
    tournament_pdf.create_pdf()
