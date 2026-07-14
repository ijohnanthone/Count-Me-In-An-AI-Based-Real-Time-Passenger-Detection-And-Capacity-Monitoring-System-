"""
Analytics service for reporting and analysis.
TODO: Implement analytics-related services.
"""


class AnalyticsService:
    """
    Service for analytics and reporting operations.
    """
    
    @staticmethod
    def calculate_average_occupancy(readings: list) -> float:
        """
        Calculate average occupancy from readings.
        """
        if not readings:
            return 0.0
        return sum(r.occupancy_percentage for r in readings) / len(readings)
    
    @staticmethod
    def find_peak_occupancy(readings: list) -> float:
        """
        Find peak occupancy from readings.
        """
        if not readings:
            return 0.0
        return max(r.occupancy_percentage for r in readings)
