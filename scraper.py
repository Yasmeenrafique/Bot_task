{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "6d1f34da",
   "metadata": {},
   "outputs": [],
   "source": [
    "import sqlite3\n",
    "from datetime import datetime\n",
    "import random\n",
    "\n",
    "def scrape_price():\n",
    "    price = random.randint(140000, 160000)\n",
    "\n",
    "    conn = sqlite3.connect(\"database.db\")\n",
    "    cursor = conn.cursor()\n",
    "\n",
    "    cursor.execute(\"\"\"\n",
    "    CREATE TABLE IF NOT EXISTS prices (\n",
    "        id INTEGER PRIMARY KEY,\n",
    "        product TEXT,\n",
    "        price INTEGER,\n",
    "        date TEXT\n",
    "    )\n",
    "    \"\"\")\n",
    "\n",
    "    cursor.execute(\"\"\"\n",
    "    INSERT INTO prices (product, price, date)\n",
    "    VALUES (?, ?, ?)\n",
    "    \"\"\", (\"iPhone 14\", price, datetime.now()))\n",
    "\n",
    "    conn.commit()\n",
    "    conn.close()\n",
    "\n",
    "    return price\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
