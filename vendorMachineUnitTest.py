import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import VendingMachine

import pytest

@pytest.fixture
def vending_machine():
    """Create a fresh vending machine for each test"""
    return VendingMachine()

def test_initial_state(vending_machine):
    """Test initial state of the vending machine"""
    assert vending_machine.get_state() == "IDLE"
    assert vending_machine.get_balance() == 0.0

def test_insert_single_coin(vending_machine):
    """Test inserting a single coin changes state"""
    vending_machine.insert_coin(0.25)
    assert vending_machine.get_state() == "ACCEPTING_COINS"
    assert vending_machine.get_balance() == 0.25

def test_insert_multiple_coins(vending_machine):
    """Test inserting multiple coins accumulates balance"""
    vending_machine.insert_coin(0.25)  # Quarter
    vending_machine.insert_coin(0.10)  # Dime
    vending_machine.insert_coin(0.05)  # Nickel
    
    assert vending_machine.get_state() == "ACCEPTING_COINS"
    assert vending_machine.get_balance() == 0.40

def test_successful_purchase_exact_change(vending_machine):
    """Test purchasing with exact change"""
    # Insert exact amount for chips ($0.75)
    vending_machine.insert_coin(0.25)
    vending_machine.insert_coin(0.25)
    vending_machine.insert_coin(0.25)
    
    # Purchase chips
    success = vending_machine.select_product("chips")
    assert success is True
    assert vending_machine.get_state() == "DISPENSING"
    
    # Collect product
    product = vending_machine.collect_product()
    assert product == "chips"
    assert vending_machine.get_state() == "IDLE"
    assert vending_machine.get_balance() == 0.0

def test_successful_purchase_with_change(vending_machine):
    """Test purchasing with change required"""
    # Insert $1.00 for chips ($0.75)
    vending_machine.insert_coin(0.25)
    vending_machine.insert_coin(0.25)
    vending_machine.insert_coin(0.25)
    vending_machine.insert_coin(0.25)
    
    # Purchase chips
    success = vending_machine.select_product("chips")
    assert success is True
    assert vending_machine.get_state() == "DISPENSING"
    
    # Collect product
    product = vending_machine.collect_product()
    assert product == "chips"
    assert vending_machine.get_state() == "GIVING_CHANGE"
    
    # Collect change
    change = vending_machine.collect_change()
    assert change == 0.25
    assert vending_machine.get_state() == "IDLE"
    assert vending_machine.get_balance() == 0.0

def test_insufficient_funds(vending_machine):
    """Test purchasing with insufficient funds"""
    # Insert only $0.50 for soda ($1.25)
    vending_machine.insert_coin(0.25)
    vending_machine.insert_coin(0.25)
    
    success = vending_machine.select_product("soda")
    assert success is False
    assert vending_machine.get_state() == "ACCEPTING_COINS"
    assert vending_machine.get_balance() == 0.50

def test_refund_functionality(vending_machine):
    """Test requesting refund"""
    # Insert some coins
    vending_machine.insert_coin(0.25)
    vending_machine.insert_coin(0.10)
    vending_machine.insert_coin(0.05)
    
    assert vending_machine.get_balance() == 0.40
    assert vending_machine.get_state() == "ACCEPTING_COINS"
    
    # Request refund
    refund = vending_machine.request_refund()
    assert refund == 0.40
    assert vending_machine.get_state() == "IDLE"
    assert vending_machine.get_balance() == 0.0

@pytest.mark.parametrize("product_name,price", [
    ("chips", 0.75),
    ("candy", 1.00),
    ("soda", 1.25)
])
def test_all_products(product_name, price):
    """Test purchasing all available products"""
    vm = VendingMachine()
    
    # Insert exact amount using quarters, dimes, and nickels
    remaining = price
    while remaining >= 0.25:
        vm.insert_coin(0.25)
        remaining = round(remaining - 0.25, 2)
    while remaining >= 0.10:
        vm.insert_coin(0.10)
        remaining = round(remaining - 0.10, 2)
    while remaining >= 0.05:
        vm.insert_coin(0.05)
        remaining = round(remaining - 0.05, 2)
    
    # Purchase and verify
    success = vm.select_product(product_name)
    assert success is True, f"Failed to purchase {product_name}"
    
    product = vm.collect_product()
    assert product == product_name
    assert vm.get_state() == "IDLE"

def test_decimal_precision(vending_machine):
    """Test that decimal precision is handled correctly"""
    # Insert coins that might cause floating point issues
    vending_machine.insert_coin(0.10)
    vending_machine.insert_coin(0.10)
    vending_machine.insert_coin(0.10)
    
    balance = vending_machine.get_balance()
    assert balance == 0.30
    
    # Add one more dime
    vending_machine.insert_coin(0.10)
    assert vending_machine.get_balance() == 0.40

def test_collect_product_when_idle(vending_machine):
    """Test collecting product when machine is idle"""
    # Should handle gracefully - either return None/empty or not crash
    result = vending_machine.collect_product()
    assert result in [None, "", "none"] or result is None

def test_collect_change_when_idle(vending_machine):
    """Test collecting change when machine is idle"""
    change = vending_machine.collect_change()
    assert change == 0.0

def test_refund_when_idle(vending_machine):
    """Test requesting refund when machine is idle"""
    refund = vending_machine.request_refund()
    assert refund == 0.0

def test_select_invalid_product(vending_machine):
    """Test selecting a product that doesn't exist"""
    vending_machine.insert_coin(0.25)
    vending_machine.insert_coin(0.25)
    
    success = vending_machine.select_product("pizza")
    assert success is False
    assert vending_machine.get_state() == "ACCEPTING_COINS"

@pytest.mark.parametrize("coin_value", [0.25, 0.10, 0.05])
def test_valid_coin_values(vending_machine, coin_value):
    """Test that all valid coin values are accepted"""
    vending_machine.insert_coin(coin_value)
    assert vending_machine.get_state() == "ACCEPTING_COINS"
    assert vending_machine.get_balance() == coin_value

def test_complete_transaction_flow(vending_machine):
    """Test a complete transaction from start to finish"""
    # Start in IDLE
    assert vending_machine.get_state() == "IDLE"
    
    # Insert coins -> ACCEPTING_COINS
    vending_machine.insert_coin(0.25)
    vending_machine.insert_coin(0.25)
    vending_machine.insert_coin(0.25)
    vending_machine.insert_coin(0.25)
    assert vending_machine.get_state() == "ACCEPTING_COINS"
    assert vending_machine.get_balance() == 1.00
    
    # Select product -> DISPENSING
    success = vending_machine.select_product("chips")
    assert success is True
    assert vending_machine.get_state() == "DISPENSING"
    
    # Collect product -> GIVING_CHANGE (since we overpaid)
    product = vending_machine.collect_product()
    assert product == "chips"
    assert vending_machine.get_state() == "GIVING_CHANGE"
    
    # Collect change -> IDLE
    change = vending_machine.collect_change()
    assert change == 0.25
    assert vending_machine.get_state() == "IDLE"
    assert vending_machine.get_balance() == 0.0

def test_refund_resets_to_idle(vending_machine):
    """Test that refund properly resets machine to idle state"""
    # Insert money and verify we're accepting coins
    vending_machine.insert_coin(0.25)
    vending_machine.insert_coin(0.50)  # Invalid coin should be handled gracefully
    vending_machine.insert_coin(0.10)
    
    # Request refund
    refund = vending_machine.request_refund()
    
    # Should be back to idle with no balance
    assert vending_machine.get_state() == "IDLE"
    assert vending_machine.get_balance() == 0.0
    assert refund >= 0  # Should return some positive amount or 0
