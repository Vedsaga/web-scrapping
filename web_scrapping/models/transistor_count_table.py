class TransistorCountTable:
    """
    This class will have 3 fields
    1. Processor
    2. Year
    3. Transistor Count
    """
    
    def __init__(self, processor_name:str, year:int, transistor_count:int ) -> None:
        self.processor_name = processor_name
        self.year = year
        self.transistor_count = transistor_count
