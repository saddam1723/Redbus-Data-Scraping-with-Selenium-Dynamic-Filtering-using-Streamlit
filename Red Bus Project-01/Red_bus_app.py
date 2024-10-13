{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "16514727-df10-4a71-8eae-8219c657a3de",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: selenium in c:\\users\\moham\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (4.25.0)\n",
      "Requirement already satisfied: urllib3<3,>=1.26 in c:\\users\\moham\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from urllib3[socks]<3,>=1.26->selenium) (2.2.3)\n",
      "Requirement already satisfied: trio~=0.17 in c:\\users\\moham\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from selenium) (0.26.2)\n",
      "Requirement already satisfied: trio-websocket~=0.9 in c:\\users\\moham\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from selenium) (0.11.1)\n",
      "Requirement already satisfied: certifi>=2021.10.8 in c:\\users\\moham\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from selenium) (2024.8.30)\n",
      "Requirement already satisfied: typing_extensions~=4.9 in c:\\users\\moham\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from selenium) (4.12.2)\n",
      "Requirement already satisfied: websocket-client~=1.8 in c:\\users\\moham\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from selenium) (1.8.0)\n",
      "Requirement already satisfied: attrs>=23.2.0 in c:\\users\\moham\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from trio~=0.17->selenium) (24.2.0)\n",
      "Requirement already satisfied: sortedcontainers in c:\\users\\moham\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from trio~=0.17->selenium) (2.4.0)\n",
      "Requirement already satisfied: idna in c:\\users\\moham\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from trio~=0.17->selenium) (3.10)\n",
      "Requirement already satisfied: outcome in c:\\users\\moham\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from trio~=0.17->selenium) (1.3.0.post0)\n",
      "Requirement already satisfied: sniffio>=1.3.0 in c:\\users\\moham\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from trio~=0.17->selenium) (1.3.1)\n",
      "Requirement already satisfied: cffi>=1.14 in c:\\users\\moham\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from trio~=0.17->selenium) (1.17.1)\n",
      "Requirement already satisfied: wsproto>=0.14 in c:\\users\\moham\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from trio-websocket~=0.9->selenium) (1.2.0)\n",
      "Requirement already satisfied: pysocks!=1.5.7,<2.0,>=1.5.6 in c:\\users\\moham\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from urllib3[socks]<3,>=1.26->selenium) (1.7.1)\n",
      "Requirement already satisfied: pycparser in c:\\users\\moham\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from cffi>=1.14->trio~=0.17->selenium) (2.22)\n",
      "Requirement already satisfied: h11<1,>=0.9.0 in c:\\users\\moham\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from wsproto>=0.14->trio-websocket~=0.9->selenium) (0.14.0)\n"
     ]
    }
   ],
   "source": [
    "!pip install selenium"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "6ea0384d-04ee-4ae9-bfb0-025dc88c3503",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: pymysql in c:\\users\\moham\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (1.1.1)\n"
     ]
    }
   ],
   "source": [
    "!pip install pymysql"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "054dd423-8b21-47a1-bf0b-86fad62e8ae7",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'streamlit'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[5], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mstreamlit\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mst\u001b[39;00m\n\u001b[0;32m      2\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mpymysql\u001b[39;00m\n\u001b[0;32m      3\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mpandas\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mpd\u001b[39;00m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'streamlit'"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pymysql\n",
    "import pandas as pd\n",
    "\n",
    "# Connect to MySQL database\n",
    "def get_connection():\n",
    "    return pymysql.connect(host='127.0.0.1', user='root', passwd='123456789', database='redbus')\n",
    "\n",
    "# Function to fetch route names starting with a specific letter, arranged alphabetically\n",
    "def fetch_route_names(connection, starting_letter):\n",
    "    query = f\"SELECT DISTINCT Route_Name FROM bus_routes WHERE Route_Name LIKE '{starting_letter}%' ORDER BY Route_Name\"\n",
    "    route_names = pd.read_sql(query, connection)['Route_Name'].tolist()\n",
    "    return route_names\n",
    "\n",
    "# Function to fetch data from MySQL based on selected Route_Name and price sort order\n",
    "def fetch_data(connection, route_name, price_sort_order):\n",
    "    price_sort_order_sql = \"ASC\" if price_sort_order == \"Low to High\" else \"DESC\"\n",
    "    query = f\"SELECT * FROM bus_routes WHERE Route_Name = %s ORDER BY Star_Rating DESC, Price {price_sort_order_sql}\"\n",
    "    df = pd.read_sql(query, connection, params=(route_name))\n",
    "    return df\n",
    "\n",
    "# Function to filter data based on Star_Rating and Bus_Type\n",
    "def filter_data(df, star_ratings, bus_types):\n",
    "    filtered_df = df[df['Star_Rating'].isin(star_ratings) & df['Bus_Type'].isin(bus_types)]\n",
    "    return filtered_df\n",
    "\n",
    "# Main Streamlit app\n",
    "def main():\n",
    "    st.header('Easy and Secure Online Bus Tickets Booking')\n",
    "\n",
    "    connection = get_connection()\n",
    "\n",
    "    try:\n",
    "        # Sidebar - Input for starting letter\n",
    "        starting_letter = st.sidebar.text_input('Enter starting letter of Route Name', 'A')\n",
    "\n",
    "        # Fetch route names starting with the specified letter\n",
    "        if starting_letter:\n",
    "            route_names = fetch_route_names(connection, starting_letter.upper())\n",
    "\n",
    "            if route_names:\n",
    "                # Sidebar - Selectbox for Route_Name\n",
    "                selected_route = st.sidebar.radio('Select Route Name', route_names)\n",
    "\n",
    "                if selected_route:\n",
    "                    # Sidebar - Selectbox for sorting preference\n",
    "                    price_sort_order = st.sidebar.selectbox('Sort by Price', ['Low to High', 'High to Low'])\n",
    "\n",
    "                    # Fetch data based on selected Route_Name and price sort order\n",
    "                    data = fetch_data(connection, selected_route, price_sort_order)\n",
    "\n",
    "                    if not data.empty:\n",
    "                        # Display data table with a subheader\n",
    "                        st.write(f\"### Data for Route: {selected_route}\")\n",
    "                        st.write(data)\n",
    "\n",
    "                        # Filter by Star_Rating and Bus_Type\n",
    "                        star_ratings = data['Star_Rating'].unique().tolist()\n",
    "                        selected_ratings = st.multiselect('Filter by Star Rating', star_ratings)\n",
    "\n",
    "                        bus_types = data['Bus_Type'].unique().tolist()\n",
    "                        selected_bus_types = st.multiselect('Filter by Bus Type', bus_types)\n",
    "\n",
    "                        if selected_ratings and selected_bus_types:\n",
    "                            filtered_data = filter_data(data, selected_ratings, selected_bus_types)\n",
    "                            # Display filtered data table with a subheader\n",
    "                            st.write(f\"### Filtered Data for Star Rating: {selected_ratings} and Bus Type: {selected_bus_types}\")\n",
    "                            st.write(filtered_data)\n",
    "                    else:\n",
    "                        st.write(f\"No data found for Route: {selected_route} with the specified price sort order.\")\n",
    "            else:\n",
    "                st.write(\"No routes found starting with the specified letter.\")\n",
    "    finally:\n",
    "        connection.close()\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f3ec3df0-5174-4b7d-9936-65b905d175ec",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0bfc7011-234c-4685-90df-6b9f316133b9",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
