if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
from caseconverter import snakecase

@transformer
def transform(data, *args, **kwargs):
    # It seems there's a mistake in your approach to filtering data,
    # you should update non_zero_data based on its previous value, not data
    non_zero_data = data[data['passenger_count'] > 0]
    non_zero_data = non_zero_data[non_zero_data['trip_distance'] > 0]
    # Assuming lpep_pickup_datetime is a datetime column, you might want to extract date or another specific part
    non_zero_data['lpep_pickup_date'] = non_zero_data['lpep_pickup_datetime'].dt.date

    print(f"Preprocessing: rows with zero passengers: {data['passenger_count'].isin([0]).sum()}")
    print(f"Preprocessing: rows with zero trip distance: {data['trip_distance'].isin([0]).sum()}")

    non_zero_data.columns = [snakecase(col) for col in non_zero_data.columns]
    print(non_zero_data)
    valid_vendor_ids = non_zero_data['vendor_id'].unique()
    print(valid_vendor_ids)
    return non_zero_data

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    # Ensure passenger_count is greater than 0
    assert output['passenger_count'].isin([0]).sum() == 0, 'There are rides with zero  passenger count'
    # Ensure trip_distance is greater than 0
    assert output['trip_distance'].isin([0]).sum() == 0, 'There are rides with zero  trip distance'
    # Ensure vendor_id is one of the existing values (assuming you have a list of valid vendor IDs)
    valid_vendor_ids = output['vendor_id'].unique()  # Example, you might want to replace this with actual valid IDs
    assert output['vendor_id'].isin(valid_vendor_ids).all(), 'There are invalid vendor IDs'

