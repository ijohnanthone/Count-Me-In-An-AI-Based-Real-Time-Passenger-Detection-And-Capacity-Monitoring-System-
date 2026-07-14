"""
Alert service for managing alerts.
TODO: Implement alert-related services.
"""


class AlertService:
    """
    Service for alert-related operations.
    """
    
    @staticmethod
    def determine_alert_severity(occupancy_percentage: float) -> str:
        """
        Determine alert severity based on occupancy percentage.
        """
        if occupancy_percentage >= 95:
            return "CRITICAL"
        elif occupancy_percentage >= 85:
            return "HIGH"
        elif occupancy_percentage >= 75:
            return "MEDIUM"
        else:
            return "LOW"
    
    @staticmethod
    def should_alert(occupancy_percentage: float, threshold: int) -> bool:
        """
        Determine if an alert should be triggered.
        """
        return occupancy_percentage >= threshold
