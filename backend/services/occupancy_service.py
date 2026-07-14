"""
Occupancy service for business logic.
TODO: Implement occupancy-related services.
"""


class OccupancyService:
    """
    Service for occupancy-related operations.
    """
    
    @staticmethod
    def calculate_occupancy_percentage(person_count: int, capacity: int) -> float:
        """
        Calculate occupancy percentage.
        """
        if capacity <= 0:
            return 0.0
        return (person_count / capacity) * 100
    
    @staticmethod
    def is_overcrowded(occupancy_percentage: float, threshold: int) -> bool:
        """
        Check if vehicle is overcrowded based on threshold.
        """
        return occupancy_percentage >= threshold
