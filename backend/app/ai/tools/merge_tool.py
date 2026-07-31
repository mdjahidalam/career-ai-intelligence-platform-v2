class MergeTool:

    @staticmethod
    def merge(*sections):

        merged = {}

        for section in sections:

            if section:

                merged.update(section)

        return merged