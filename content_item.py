class TechnologyUpdate:
    """
    Represents one technology update submitted by an employee.
    """

    def __init__(
        self,
        employee_name,
        department,
        category,
        news_title,
        summary,
        why_it_matters,
        source_link,
        status="Pending Review"
    ):
        self.employee_name = employee_name
        self.department = department
        self.category = category
        self.news_title = news_title
        self.summary = summary
        self.why_it_matters = why_it_matters
        self.source_link = source_link
        self.status = status

    def to_dict(self):
        """
        Convert the TechnologyUpdate object into a dictionary
        so it can be saved in a JSON file.
        """
        return {
            "employee_name": self.employee_name,
            "department": self.department,
            "category": self.category,
            "news_title": self.news_title,
            "summary": self.summary,
            "why_it_matters": self.why_it_matters,
            "source_link": self.source_link,
            "status": self.status
        }

    @staticmethod
    def from_dict(data):
        """
        Create a TechnologyUpdate object from a dictionary
        loaded from a JSON file.
        """
        return TechnologyUpdate(
            data.get("employee_name", ""),
            data.get("department", ""),
            data.get("category", ""),
            data.get("news_title", ""),
            data.get("summary", ""),
            data.get("why_it_matters", ""),
            data.get("source_link", ""),
            data.get("status", "Pending Review")
        )