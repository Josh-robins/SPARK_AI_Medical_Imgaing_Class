def create_modalities_list():
    """
    Exercise 6: Basic List Operations
    Create a list with ["X-ray", "CT", "MRI", "Ultrasound"] and add "PET" to it.
    
    Returns:
        list: List of imaging modalities including PET
    """
    # TODO: Create the initial list
    imaging_modalities = None
    
    # TODO: Add "PET" to the list
    
    return imaging_modalities


def get_first_two_times():
    """
    Exercise 7: Indexing and Slicing Lists
    From scan_times = [12.5, 8.0, 15.2, 10.3], get the first two values.
    
    Returns:
        list: First two scan times
    """
    scan_times = [12.5, 8.0, 15.2, 10.3]
    
    # TODO: Return first two elements using slicing
    return None


def update_scan_quality():
    """
    Exercise 8: Modifying Lists
    In scan_quality = ["high", "medium", "low", "medium"], replace "low" with "high".
    
    Returns:
        list: Updated scan quality list
    """
    scan_quality = ["high", "medium", "low", "medium"]
    
    # TODO: Replace "low" with "high"
    
    return scan_quality


def get_patient_info():
    """
    Exercise 9: Create a dictionary with patient info
    Keys: "ID" (101), "Name" ("Alice"), "Age" (45), "Modality" ("MRI")
    
    Returns:
        dict: Patient information dictionary
    """
    # TODO: Create and return the patient dictionary
    return None


def update_scan_parameters():
    """
    Exercise 10: Updating Dictionary Entries
    Update slice_thickness to 1.5 and contrast_used to True in the scan_parameters dictionary.
    
    Returns:
        dict: Updated scan parameters dictionary
    """
    scan_parameters = {
        "modality": "CT",
        "slice_thickness": 3.0,
        "contrast_used": False
    }
    
    # TODO: Update the dictionary values
    
    return scan_parameters


def create_image_metadata():
    """
    Exercise 11: Create a dictionary with image metadata
    Keys: "resolution" ("512x512"), "scan_type" ("MRI"), "bit_depth" (16)
    
    Returns:
        dict: Image metadata dictionary
    """
    # TODO: Create and return the metadata dictionary
    return None


def create_patients_data():
    """
    Exercise 12: Create a nested dictionary for two patients
    Patient 101: {"Name": "Alice", "Age": 45, "Scan_Type": "MRI"}
    Patient 102: {"Name": "Bob", "Age": 50, "Scan_Type": "CT"}
    
    Returns:
        dict: Nested dictionary with patient data
    """
    # TODO: Create and return the nested dictionary
    return None
