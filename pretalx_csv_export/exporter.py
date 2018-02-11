import csv
import io


class CSVExporter:
    pass
    def render(self, form_data):
        output = io.StringIO()
        writer = csv.writer(output, quoting=csv.QUOTE_NONNUMERIC, delimiter=',')
        submissions = list(self.event.submissions.all())

        headers = ['Code', 'Title', 'Abstract', 'Description', 'Speakers', 'State']
        writer.writerow(headers)

        for submission in submissions:
            row = [
                submission.code, submission.title, submission.abstract, submission.description,
                submission.display_speaker_names, submission.state,
            ]
            writer.writerow(row)

        return f'{self.event.slug}-submissions.csv', 'text/csv', output.getvalue().encode('utf-8')
