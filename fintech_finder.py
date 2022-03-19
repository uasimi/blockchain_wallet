# Cryptocurrency Wallet

import streamlit as st
from dataclasses import dataclass
from typing import Any, List
from web3 import Web3
w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))
from crypto_wallet import generate_account, get_balance, send_transaction

candidate_database = {
    "Lane": ["Lane", "0xaC8eB8B2ed5C4a0fC41a84Ee4950F417f67029F0", "4.3", .20, "Images/lane.jpeg"],
    "Ash": ["Ash", "0x2422858F9C4480c2724A309D58Ffd7Ac8bF65396", "5.0", .33, "Images/ash.jpeg"],
    "Jo": ["Jo", "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45", "4.7", .19, "Images/jo.jpeg"],
    "Kendall": ["Kendall", "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45", "4.1", .16, "Images/kendall.jpeg"]
}

people = ["Lane", "Ash", "Jo", "Kendall"]

def get_people(w3):
    """Display the database of Fintech Finders candidate information."""
    db_list = list(candidate_database.values())

    for number in range(len(people)):
        st.image(db_list[number][4], width=200)
        st.write("Name: ", db_list[number][0])
        st.write("Ethereum Account Address: ", db_list[number][1])
        st.write("FinTech Finder Rating: ", db_list[number][2])
        st.write("Hourly Rate per Ether: ", db_list[number][3], "eth")
        st.text(" \n")

st.markdown("# Fintech Finder!")
st.markdown("## Hire A Fintech Professional!")
st.text(" \n")
st.sidebar.markdown("## Client Account Address and Ethernet Balance in Ether")

account = generate_account()
st.sidebar.write(account.address)

st.sidebar.write(get_balance(w3, account.address))

person = st.sidebar.selectbox('Select a Person', people)
hours = st.sidebar.number_input("Number of Hours")

st.sidebar.markdown("## Candidate Name, Hourly Rate, and Ethereum Address")

candidate = candidate_database[person][0]
st.sidebar.write(candidate)

hourly_rate = candidate_database[person][3]
st.sidebar.write(hourly_rate)

candidate_address = candidate_database[person][1]
st.sidebar.write(candidate_address)

st.sidebar.markdown("## Total Wage in Ether")

wage = candidate_database[person][3] * hours
st.sidebar.write(wage)

if st.sidebar.button("Send Transaction"):
    transaction_hash = send_transaction(w3, account, candidate_address, wage)
    st.sidebar.markdown("#### Validated Transaction Hash")
    st.sidebar.write(transaction_hash)
    st.balloons()

get_people(w3)

