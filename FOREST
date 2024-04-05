{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "3a76228b-d7b9-46bd-b3a7-a464cb312a74",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "058b1c91-3734-42b7-8722-fba56453ec77",
   "metadata": {},
   "outputs": [],
   "source": [
    "data = pd.read_csv('amazon.csv',encoding=\"iso-8859-1\",parse_dates=['date'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "f90810c3-3dc3-4866-875a-2d151ce8e3aa",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "year               int64\n",
       "state             object\n",
       "month             object\n",
       "number           float64\n",
       "date      datetime64[ns]\n",
       "dtype: object"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "0ab87fb1-a385-496a-8fd9-0499111b9e37",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>year</th>\n",
       "      <th>state</th>\n",
       "      <th>month</th>\n",
       "      <th>number</th>\n",
       "      <th>date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1998</td>\n",
       "      <td>Acre</td>\n",
       "      <td>Janeiro</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1998-01-01</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1999</td>\n",
       "      <td>Acre</td>\n",
       "      <td>Janeiro</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1999-01-01</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2000</td>\n",
       "      <td>Acre</td>\n",
       "      <td>Janeiro</td>\n",
       "      <td>0.0</td>\n",
       "      <td>2000-01-01</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2001</td>\n",
       "      <td>Acre</td>\n",
       "      <td>Janeiro</td>\n",
       "      <td>0.0</td>\n",
       "      <td>2001-01-01</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2002</td>\n",
       "      <td>Acre</td>\n",
       "      <td>Janeiro</td>\n",
       "      <td>0.0</td>\n",
       "      <td>2002-01-01</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   year state    month  number       date\n",
       "0  1998  Acre  Janeiro     0.0 1998-01-01\n",
       "1  1999  Acre  Janeiro     0.0 1999-01-01\n",
       "2  2000  Acre  Janeiro     0.0 2000-01-01\n",
       "3  2001  Acre  Janeiro     0.0 2001-01-01\n",
       "4  2002  Acre  Janeiro     0.0 2002-01-01"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "685506ac-d3bd-4899-b04a-f3d2e6dc978e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>year</th>\n",
       "      <th>state</th>\n",
       "      <th>month</th>\n",
       "      <th>number</th>\n",
       "      <th>date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>6449</th>\n",
       "      <td>2012</td>\n",
       "      <td>Tocantins</td>\n",
       "      <td>Dezembro</td>\n",
       "      <td>128.0</td>\n",
       "      <td>2012-01-01</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6450</th>\n",
       "      <td>2013</td>\n",
       "      <td>Tocantins</td>\n",
       "      <td>Dezembro</td>\n",
       "      <td>85.0</td>\n",
       "      <td>2013-01-01</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6451</th>\n",
       "      <td>2014</td>\n",
       "      <td>Tocantins</td>\n",
       "      <td>Dezembro</td>\n",
       "      <td>223.0</td>\n",
       "      <td>2014-01-01</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6452</th>\n",
       "      <td>2015</td>\n",
       "      <td>Tocantins</td>\n",
       "      <td>Dezembro</td>\n",
       "      <td>373.0</td>\n",
       "      <td>2015-01-01</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6453</th>\n",
       "      <td>2016</td>\n",
       "      <td>Tocantins</td>\n",
       "      <td>Dezembro</td>\n",
       "      <td>119.0</td>\n",
       "      <td>2016-01-01</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      year      state     month  number       date\n",
       "6449  2012  Tocantins  Dezembro   128.0 2012-01-01\n",
       "6450  2013  Tocantins  Dezembro    85.0 2013-01-01\n",
       "6451  2014  Tocantins  Dezembro   223.0 2014-01-01\n",
       "6452  2015  Tocantins  Dezembro   373.0 2015-01-01\n",
       "6453  2016  Tocantins  Dezembro   119.0 2016-01-01"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.tail()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "998281b0-13f7-42d8-8d62-70fd9bd089ed",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(6454, 5)"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "1bd136c2-dbd7-4644-875e-277580e7baa5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 6454 entries, 0 to 6453\n",
      "Data columns (total 5 columns):\n",
      " #   Column  Non-Null Count  Dtype         \n",
      "---  ------  --------------  -----         \n",
      " 0   year    6454 non-null   int64         \n",
      " 1   state   6454 non-null   object        \n",
      " 2   month   6454 non-null   object        \n",
      " 3   number  6454 non-null   float64       \n",
      " 4   date    6454 non-null   datetime64[ns]\n",
      "dtypes: datetime64[ns](1), float64(1), int64(1), object(2)\n",
      "memory usage: 252.2+ KB\n"
     ]
    }
   ],
   "source": [
    "data.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "9fa647c4-9f13-4b23-9c39-29d0f585ddba",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.duplicated().any()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "4df40ab2-afe4-445e-a33f-751599bd1023",
   "metadata": {},
   "outputs": [],
   "source": [
    "data=data.drop_duplicates()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "4b432d49-9608-42ea-9f4b-0a98df27ce51",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(6422, 5)"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "967dd00b-5760-431d-a1df-088d5196cf14",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "year      0\n",
       "state     0\n",
       "month     0\n",
       "number    0\n",
       "date      0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "82d9c785-8fee-4d7c-9d93-2ce32cb57e6d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>year</th>\n",
       "      <th>state</th>\n",
       "      <th>month</th>\n",
       "      <th>number</th>\n",
       "      <th>date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>6422.000000</td>\n",
       "      <td>6422</td>\n",
       "      <td>6422</td>\n",
       "      <td>6422.000000</td>\n",
       "      <td>6422</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>unique</th>\n",
       "      <td>NaN</td>\n",
       "      <td>23</td>\n",
       "      <td>12</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>top</th>\n",
       "      <td>NaN</td>\n",
       "      <td>Rio</td>\n",
       "      <td>Agosto</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>freq</th>\n",
       "      <td>NaN</td>\n",
       "      <td>697</td>\n",
       "      <td>540</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>2007.490969</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>108.815178</td>\n",
       "      <td>2007-06-29 10:46:40.622859008</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1998.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1998-01-01 00:00:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>2003.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>2003-01-01 00:00:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>2007.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>24.497000</td>\n",
       "      <td>2007-01-01 00:00:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>2012.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>114.000000</td>\n",
       "      <td>2012-01-01 00:00:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>2017.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>998.000000</td>\n",
       "      <td>2017-01-01 00:00:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>5.731806</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>191.142482</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               year state   month       number                           date\n",
       "count   6422.000000  6422    6422  6422.000000                           6422\n",
       "unique          NaN    23      12          NaN                            NaN\n",
       "top             NaN   Rio  Agosto          NaN                            NaN\n",
       "freq            NaN   697     540          NaN                            NaN\n",
       "mean    2007.490969   NaN     NaN   108.815178  2007-06-29 10:46:40.622859008\n",
       "min     1998.000000   NaN     NaN     0.000000            1998-01-01 00:00:00\n",
       "25%     2003.000000   NaN     NaN     3.000000            2003-01-01 00:00:00\n",
       "50%     2007.000000   NaN     NaN    24.497000            2007-01-01 00:00:00\n",
       "75%     2012.000000   NaN     NaN   114.000000            2012-01-01 00:00:00\n",
       "max     2017.000000   NaN     NaN   998.000000            2017-01-01 00:00:00\n",
       "std        5.731806   NaN     NaN   191.142482                            NaN"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.describe(include='all')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "5bf3ac94-7c7c-4395-bd2e-7a1482fad903",
   "metadata": {},
   "outputs": [],
   "source": [
    "data['month_new']=data['month'].map({'Janeiro':'jan',\n",
    "                                     'Março': 'march',\n",
    "                                     'Abril': 'april',\n",
    "                                     'Maio': 'may', 'Junho':'jun',\n",
    "                                     'Julho': 'july',\n",
    "                                     'Agosto':'august',\n",
    "                                     'Setembro': 'sep',\n",
    "                                     'Outubro':'oct',\n",
    "                                     'Novembro': 'nov',\n",
    "                                     'Dezembro':'dec'\n",
    "\n",
    "})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "2790fdc8-e746-46aa-8c58-f6d091b531e5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>year</th>\n",
       "      <th>state</th>\n",
       "      <th>month</th>\n",
       "      <th>number</th>\n",
       "      <th>date</th>\n",
       "      <th>month_new</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1998</td>\n",
       "      <td>Acre</td>\n",
       "      <td>Janeiro</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1998-01-01</td>\n",
       "      <td>jan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1999</td>\n",
       "      <td>Acre</td>\n",
       "      <td>Janeiro</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1999-01-01</td>\n",
       "      <td>jan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2000</td>\n",
       "      <td>Acre</td>\n",
       "      <td>Janeiro</td>\n",
       "      <td>0.0</td>\n",
       "      <td>2000-01-01</td>\n",
       "      <td>jan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2001</td>\n",
       "      <td>Acre</td>\n",
       "      <td>Janeiro</td>\n",
       "      <td>0.0</td>\n",
       "      <td>2001-01-01</td>\n",
       "      <td>jan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2002</td>\n",
       "      <td>Acre</td>\n",
       "      <td>Janeiro</td>\n",
       "      <td>0.0</td>\n",
       "      <td>2002-01-01</td>\n",
       "      <td>jan</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   year state    month  number       date month_new\n",
       "0  1998  Acre  Janeiro     0.0 1998-01-01       jan\n",
       "1  1999  Acre  Janeiro     0.0 1999-01-01       jan\n",
       "2  2000  Acre  Janeiro     0.0 2000-01-01       jan\n",
       "3  2001  Acre  Janeiro     0.0 2001-01-01       jan\n",
       "4  2002  Acre  Janeiro     0.0 2002-01-01       jan"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "d7ec8108-8bac-45ad-b1a2-838eae97c21c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>year</th>\n",
       "      <th>state</th>\n",
       "      <th>month</th>\n",
       "      <th>number</th>\n",
       "      <th>date</th>\n",
       "      <th>month_new</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>6449</th>\n",
       "      <td>2012</td>\n",
       "      <td>Tocantins</td>\n",
       "      <td>Dezembro</td>\n",
       "      <td>128.0</td>\n",
       "      <td>2012-01-01</td>\n",
       "      <td>dec</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6450</th>\n",
       "      <td>2013</td>\n",
       "      <td>Tocantins</td>\n",
       "      <td>Dezembro</td>\n",
       "      <td>85.0</td>\n",
       "      <td>2013-01-01</td>\n",
       "      <td>dec</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6451</th>\n",
       "      <td>2014</td>\n",
       "      <td>Tocantins</td>\n",
       "      <td>Dezembro</td>\n",
       "      <td>223.0</td>\n",
       "      <td>2014-01-01</td>\n",
       "      <td>dec</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6452</th>\n",
       "      <td>2015</td>\n",
       "      <td>Tocantins</td>\n",
       "      <td>Dezembro</td>\n",
       "      <td>373.0</td>\n",
       "      <td>2015-01-01</td>\n",
       "      <td>dec</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6453</th>\n",
       "      <td>2016</td>\n",
       "      <td>Tocantins</td>\n",
       "      <td>Dezembro</td>\n",
       "      <td>119.0</td>\n",
       "      <td>2016-01-01</td>\n",
       "      <td>dec</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      year      state     month  number       date month_new\n",
       "6449  2012  Tocantins  Dezembro   128.0 2012-01-01       dec\n",
       "6450  2013  Tocantins  Dezembro    85.0 2013-01-01       dec\n",
       "6451  2014  Tocantins  Dezembro   223.0 2014-01-01       dec\n",
       "6452  2015  Tocantins  Dezembro   373.0 2015-01-01       dec\n",
       "6453  2016  Tocantins  Dezembro   119.0 2016-01-01       dec"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.tail()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "cebb0e0d-d5be-40a2-bcbe-f4071fc3b0ec",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(6422, 6)"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "3b0b74fb-d467-4050-9b87-5b78d3732d55",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['year', 'state', 'month', 'number', 'date', 'month_new'], dtype='object')"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "1da8fbe0-bee3-49b1-83a0-29b502f08ec7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>month_new</th>\n",
       "      <th>number</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>april</td>\n",
       "      <td>28184.770</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>august</td>\n",
       "      <td>88050.435</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>dec</td>\n",
       "      <td>57535.480</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>jan</td>\n",
       "      <td>47681.844</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>july</td>\n",
       "      <td>92319.113</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>jun</td>\n",
       "      <td>55997.675</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>march</td>\n",
       "      <td>30709.405</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>may</td>\n",
       "      <td>34725.363</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>nov</td>\n",
       "      <td>85508.054</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>oct</td>\n",
       "      <td>88681.579</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>sep</td>\n",
       "      <td>58578.305</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   month_new     number\n",
       "0      april  28184.770\n",
       "1     august  88050.435\n",
       "2        dec  57535.480\n",
       "3        jan  47681.844\n",
       "4       july  92319.113\n",
       "5        jun  55997.675\n",
       "6      march  30709.405\n",
       "7        may  34725.363\n",
       "8        nov  85508.054\n",
       "9        oct  88681.579\n",
       "10       sep  58578.305"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data1=data.groupby('month_new')['number'].sum().reset_index()\n",
    "data1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "6b4b3db5-fbc8-43af-bf66-89137aa32b56",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: xlabel='month_new', ylabel='number'>"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABTUAAAHACAYAAABzmYwsAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjguMCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy81sbWrAAAACXBIWXMAAA9hAAAPYQGoP6dpAABB0ElEQVR4nO3dffyW8/038NdXd5L66kYla3KTu5WyslSbspC5yc2uGVkYGmvLothcbOJHbov9uOYmRj+x7PoZdrlpxWgiRYRItoaylYx0g1XqvP7wc863knxXfR16Ph+P87GO43gfx/k+zs/OU+erz3kcFaVSqRQAAAAAgILYrKYbAAAAAAD4LISaAAAAAEChCDUBAAAAgEIRagIAAAAAhSLUBAAAAAAKRagJAAAAABSKUBMAAAAAKBShJgAAAABQKLVruoEvkpUrV+bvf/97GjZsmIqKippuBwAAAAAKpVQqZfHixWnVqlU22+yT52MKNdejv//972ndunVNtwEAAAAAhTZnzpx86Utf+sTtQs31qGHDhkk+fNEbNWpUw90AAAAAQLEsWrQorVu3Ludsn0SouR599JPzRo0aCTUBAAAAoJo+7dKObhQEAAAAABSKUBMAAAAAKBShJgAAAABQKEJNAAAAAKBQhJoAAAAAQKEINQEAAACAQhFqAgAAAACFItQEAAAAAApFqAkAAAAAFIpQEwAAAAAoFKEmAAAAAFAoQk0AAAAAoFCEmgAAAABAoQg1AQAAAIBCEWoCAAAAAIVSu6YbAAA2Xd+659SabmGT8MBh19V0CwAAsF6ZqQkAAAAAFIpQEwAAAAAoFKEmAAAAAFAoQk0AAAAAoFCEmgAAAABAoQg1AQAAAIBCEWoCAAAAAIUi1AQAAAAACkWoCQAAAAAUilATAAAAACgUoSYAAAAAUChCTQAAAACgUISaAAAAAECh1K7pBgAAAACK6KVfvVHTLWwydh3QoqZb4HPGTE0AAAAAoFCEmgAAAABAofj5OfwbZl19WE23sEnYceA9Nd0CAAAA8DlipiYAAAAAUChCTQAAAACgUISaAAAAAEChCDUBAAAAgEIRagIAAAAAhSLUBAAAAAAKRagJAAAAABSKUBMAAAAAKBShJgAAAABQKLVrugEAAADYVP32zn/UdAubhKO+3aymWwDWMzM1AQAAAIBCEWoCAAAAAIUi1AQAAAAACkWoCQAAAAAUilATAAAAACgUoSYAAAAAUChCTQAAAACgUISaAAAAAEChCDUBAAAAgEIRagIAAAAAhSLUBAAAAAAKRagJAAAAABSKUBMAAAAAKBShJgAAAABQKEJNAAAAAKBQhJoAAAAAQKEINQEAAACAQqnRUPODDz7Iueeem+233z7169fPDjvskAsuuCArV64s15RKpQwdOjStWrVK/fr107Nnz7zwwgtVjrN06dIMHDgwzZo1S4MGDdKnT5+8/vrrVWoWLFiQfv36pbKyMpWVlenXr1/eeeedKjWzZ8/OoYcemgYNGqRZs2Y57bTTsmzZsg12/gAAAADAZ1ejoeall16a6667Ltdcc01mzJiRyy67LJdffnmuvvrqcs1ll12WESNG5JprrsmTTz6Zli1bZv/998/ixYvLNYMGDcpdd92VMWPGZOLEiVmyZEkOOeSQrFixolzTt2/fTJs2LWPHjs3YsWMzbdq09OvXr7x9xYoVOfjgg/Puu+9m4sSJGTNmTO68884MHjx447wYAAAAAMA6qV2TTz5p0qQcdthhOfjgg5Mkbdq0yW9+85s89dRTST6cpXnVVVflnHPOyZFHHpkkGTVqVFq0aJHbb789p5xyShYuXJibbropt956a/bbb78kyejRo9O6des8+OCD6d27d2bMmJGxY8fmiSeeSJcuXZIkI0eOTNeuXTNz5szssssuGTduXF588cXMmTMnrVq1SpIMHz48J5xwQi666KI0atRoY788AAAAAMAa1OhMza9//et56KGH8vLLLydJnn322UycODEHHXRQkuSVV17JvHnzcsABB5T3qVevXnr06JHHH388STJ16tQsX768Sk2rVq3Srl27cs2kSZNSWVlZDjSTZO+9905lZWWVmnbt2pUDzSTp3bt3li5dmqlTp66x/6VLl2bRokVVHgAAAADAhlWjMzV/+tOfZuHChdl1111Tq1atrFixIhdddFGOOeaYJMm8efOSJC1atKiyX4sWLfLaa6+Va+rWrZvGjRuvVvPR/vPmzUvz5s1Xe/7mzZtXqVn1eRo3bpy6deuWa1Z18cUX5/zzz/+spw0AAAAA/BtqdKbmHXfckdGjR+f222/P008/nVGjRuWKK67IqFGjqtRVVFRUWS6VSqutW9WqNWuqr07Nx5199tlZuHBh+TFnzpy19gQAAAAA/PtqdKbmmWeemZ/97Gc5+uijkyTt27fPa6+9losvvjjHH398WrZsmeTDWZTbbLNNeb/58+eXZ1W2bNkyy5Yty4IFC6rM1pw/f366detWrnnjjTdWe/4333yzynEmT55cZfuCBQuyfPny1WZwfqRevXqpV69edU8fAAAAAKiGGp2p+d5772Wzzaq2UKtWraxcuTJJsv3226dly5YZP358efuyZcsyYcKEcmDZqVOn1KlTp0rN3LlzM3369HJN165ds3DhwkyZMqVcM3ny5CxcuLBKzfTp0zN37txyzbhx41KvXr106tRpPZ85AAAAAFBdNTpT89BDD81FF12UL3/5y/nKV76SZ555JiNGjMiJJ56Y5MOfgw8aNCjDhg1L27Zt07Zt2wwbNixbbLFF+vbtmySprKzMSSedlMGDB6dp06Zp0qRJhgwZkvbt25fvhr7bbrvlwAMPTP/+/XP99dcnSX7wgx/kkEMOyS677JIkOeCAA7L77runX79+ufzyy/P2229nyJAh6d+/vzufAwAAAMDnSI2GmldffXV+/vOfZ8CAAZk/f35atWqVU045Jb/4xS/KNWeddVbef//9DBgwIAsWLEiXLl0ybty4NGzYsFxz5ZVXpnbt2jnqqKPy/vvvp1evXrnllltSq1atcs1tt92W0047rXyX9D59+uSaa64pb69Vq1buu+++DBgwIN27d0/9+vXTt2/fXHHFFRvhlQAAAAAA1lVFqVQq1XQTXxSLFi1KZWVlFi5caHbnJmLW1YfVdAubhB0H3lPTLQAbyLfuObWmW9gkPHDYdTXdAgCf4Ld3/qOmW9gkHPXtZhvkuC/9avX7d7Bh7Dpgzfc74YtnXfO1Gr2mJgAAAADAZyXUBAAAAAAKRagJAAAAABSKUBMAAAAAKBShJgAAAABQKEJNAAAAAKBQhJoAAAAAQKEINQEAAACAQhFqAgAAAACFItQEAAAAAApFqAkAAAAAFIpQEwAAAAAoFKEmAAAAAFAoQk0AAAAAoFCEmgAAAABAoQg1AQAAAIBCEWoCAAAAAIUi1AQAAAAACkWoCQAAAAAUilATAAAAACgUoSYAAAAAUChCTQAAAACgUISaAAAAAEChCDUBAAAAgEIRagIAAAAAhSLUBAAAAAAKRagJAAAAABSKUBMAAAAAKBShJgAAAABQKEJNAAAAAKBQhJoAAAAAQKEINQEAAACAQhFqAgAAAACFItQEAAAAAApFqAkAAAAAFIpQEwAAAAAoFKEmAAAAAFAoQk0AAAAAoFCEmgAAAABAoQg1AQAAAIBCEWoCAAAAAIUi1AQAAAAACkWoCQAAAAAUilATAAAAACgUoSYAAAAAUChCTQAAAACgUISaAAAAAEChCDUBAAAAgEIRagIAAAAAhSLUBAAAAAAKRagJAAAAABSKUBMAAAAAKBShJgAAAABQKEJNAAAAAKBQhJoAAAAAQKEINQEAAACAQhFqAgAAAACFItQEAAAAAApFqAkAAAAAFIpQEwAAAAAoFKEmAAAAAFAoQk0AAAAAoFCEmgAAAABAoQg1AQAAAIBCEWoCAAAAAIUi1AQAAAAACkWoCQAAAAAUilATAAAAACiUGg81//a3v+V73/temjZtmi222CIdO3bM1KlTy9tLpVKGDh2aVq1apX79+unZs2deeOGFKsdYunRpBg4cmGbNmqVBgwbp06dPXn/99So1CxYsSL9+/VJZWZnKysr069cv77zzTpWa2bNn59BDD02DBg3SrFmznHbaaVm2bNkGO3cAAAAA4LOr0VBzwYIF6d69e+rUqZMHHnggL774YoYPH56tttqqXHPZZZdlxIgRueaaa/Lkk0+mZcuW2X///bN48eJyzaBBg3LXXXdlzJgxmThxYpYsWZJDDjkkK1asKNf07ds306ZNy9ixYzN27NhMmzYt/fr1K29fsWJFDj744Lz77ruZOHFixowZkzvvvDODBw/eKK8FAAAAALBuatfkk1966aVp3bp1br755vK6Nm3alP9cKpVy1VVX5ZxzzsmRRx6ZJBk1alRatGiR22+/PaecckoWLlyYm266Kbfeemv222+/JMno0aPTunXrPPjgg+ndu3dmzJiRsWPH5oknnkiXLl2SJCNHjkzXrl0zc+bM7LLLLhk3blxefPHFzJkzJ61atUqSDB8+PCeccEIuuuiiNGrUaCO9KgAAAADA2tToTM3f//736dy5c77zne+kefPm2XPPPTNy5Mjy9ldeeSXz5s3LAQccUF5Xr1699OjRI48//niSZOrUqVm+fHmVmlatWqVdu3blmkmTJqWysrIcaCbJ3nvvncrKyio17dq1KweaSdK7d+8sXbq0ys/hP27p0qVZtGhRlQcAAAAAsGHVaKj517/+Nddee23atm2bP/zhDzn11FNz2mmn5b/+67+SJPPmzUuStGjRosp+LVq0KG+bN29e6tatm8aNG6+1pnnz5qs9f/PmzavUrPo8jRs3Tt26dcs1q7r44ovL1+isrKxM69atP+tLAAAAAAB8RjUaaq5cuTJf/epXM2zYsOy555455ZRT0r9//1x77bVV6ioqKqosl0ql1datatWaNdVXp+bjzj777CxcuLD8mDNnzlp7AgAAAAD+fTUaam6zzTbZfffdq6zbbbfdMnv27CRJy5Ytk2S1mZLz588vz6ps2bJlli1blgULFqy15o033ljt+d98880qNas+z4IFC7J8+fLVZnB+pF69emnUqFGVBwAAAACwYdVoqNm9e/fMnDmzyrqXX3452223XZJk++23T8uWLTN+/Pjy9mXLlmXChAnp1q1bkqRTp06pU6dOlZq5c+dm+vTp5ZquXbtm4cKFmTJlSrlm8uTJWbhwYZWa6dOnZ+7cueWacePGpV69eunUqdN6PnMAAAAAoLpq9O7np59+erp165Zhw4blqKOOypQpU3LDDTfkhhtuSPLhz8EHDRqUYcOGpW3btmnbtm2GDRuWLbbYIn379k2SVFZW5qSTTsrgwYPTtGnTNGnSJEOGDEn79u3Ld0PfbbfdcuCBB6Z///65/vrrkyQ/+MEPcsghh2SXXXZJkhxwwAHZfffd069fv1x++eV5++23M2TIkPTv398MTAAAAAD4HKnRUHOvvfbKXXfdlbPPPjsXXHBBtt9++1x11VU59thjyzVnnXVW3n///QwYMCALFixIly5dMm7cuDRs2LBcc+WVV6Z27do56qij8v7776dXr1655ZZbUqtWrXLNbbfdltNOO618l/Q+ffrkmmuuKW+vVatW7rvvvgwYMCDdu3dP/fr107dv31xxxRUb4ZUAAAAAANZVRalUKtV0E18UixYtSmVlZRYuXGh25yZi1tWH1XQLm4QdB95T0y0AG8i37jm1plvYJDxw2HU13QIAn+C3d/6jplvYJBz17WYb5Lgv/Wr1+3ewYew6YM33O/l3vXHVlE8v4t/WYtDX1rl2XfO1Gr2mJgAAAADAZyXUBAAAAAAKRagJAAAAABRKjd4oCKAm3fvrb9V0C5uMQ058oKZbAAAA4AvETE0AAAAAoFCEmgAAAABAoQg1AQAAAIBCEWoCAAAAAIUi1AQAAAAACsXdzwEAqLaD77y+plvYJNz37VNqugUAgM8VMzUBAAAAgEIRagIAAAAAhSLUBAAAAAAKRagJAAAAABSKUBMAAAAAKJTPHGqWSqW89tpref/99zdEPwAAAAAAa1WtULNt27Z5/fXXN0Q/AAAAAABr9ZlDzc022yxt27bNW2+9tSH6AQAAAABYq2pdU/Oyyy7LmWeemenTp6/vfgAAAAAA1qp2dXb63ve+l/feey8dOnRI3bp1U79+/Srb33777fXSHAAAAADAqqoVal511VXruQ0AAAAAgHVTrVDz+OOPX999AAAAAACsk2pdUzNJZs2alXPPPTfHHHNM5s+fnyQZO3ZsXnjhhfXWHAAAAADAqqoVak6YMCHt27fP5MmT87vf/S5LlixJkjz33HM577zz1muDAAAAAAAfV61Q82c/+1kuvPDCjB8/PnXr1i2v33fffTNp0qT11hwAAAAAwKqqFWo+//zzOeKII1Zbv/XWW+ett976t5sCAAAAAPgk1Qo1t9pqq8ydO3e19c8880y23Xbbf7spAAAAAIBPUq1Qs2/fvvnpT3+aefPmpaKiIitXrsxjjz2WIUOG5LjjjlvfPQIAAAAAlFUr1Lzooovy5S9/Odtuu22WLFmS3XffPfvss0+6deuWc889d333CAAAAABQVrs6O9WpUye33XZbLrjggjzzzDNZuXJl9txzz7Rt23Z99wcAAAAAUEW1Qs2P7Ljjjtlhhx2SJBUVFeulIQAAAACAtanWz8+T5Kabbkq7du2y+eabZ/PNN0+7du1y4403rs/eAAAAAABWU62Zmj//+c9z5ZVXZuDAgenatWuSZNKkSTn99NPz6quv5sILL1yvTQIAAAAAfKRaoea1116bkSNH5phjjimv69OnT/bYY48MHDhQqAkAAAAAbDDV+vn5ihUr0rlz59XWd+rUKR988MG/3RQAAAAAwCepVqj5ve99L9dee+1q62+44YYce+yx/3ZTAAAAAACfZJ1/fn7GGWeU/1xRUZEbb7wx48aNy957750keeKJJzJnzpwcd9xx679LAAAAAID/sc6h5jPPPFNluVOnTkmSWbNmJUm23nrrbL311nnhhRfWY3sAAAAAAFWtc6j58MMPb8g+AAAAAADWSbWuqQkAAAAAUFPWeabmx/3zn//M1VdfnYcffjjz58/PypUrq2x/+umn10tzAAAAAACrqlaoeeKJJ2b8+PH5X//rf+VrX/taKioq1ndfAAAAAABrVK1Q87777sv999+f7t27r+9+AGCdXXl775puYZNwet8/1HQLAAAAVVTrmprbbrttGjZsuL57AQAAAAD4VNUKNYcPH56f/vSnee2119Z3PwAAAAAAa1Wtn5937tw5//znP7PDDjtkiy22SJ06dapsf/vtt9dLcwAAAAAAq6pWqHnMMcfkb3/7W4YNG5YWLVq4URAAAAAAsNFUK9R8/PHHM2nSpHTo0GF99wMAAAAAsFbVuqbmrrvumvfff3999wIAAAAA8KmqFWpecsklGTx4cB555JG89dZbWbRoUZUHAAAAAMCGUq2fnx944IFJkl69elVZXyqVUlFRkRUrVvz7nQEAAAAArEG1Qs2HH354ffcBAAAAALBOqhVq9ujRY333AQAAAACwTqoVav7pT39a6/Z99tmnWs0AAAAAAHyaaoWaPXv2XG1dRUVF+c+uqQkAAAAAbCjVuvv5ggULqjzmz5+fsWPHZq+99sq4cePWd48AAAAAAGXVmqlZWVm52rr9998/9erVy+mnn56pU6f+240BAAAAAKxJtWZqfpKtt946M2fOXJ+HBAAAAACoolozNZ977rkqy6VSKXPnzs0ll1ySDh06rJfGAAAAAADWpFqhZseOHVNRUZFSqVRl/d57751f//rX66UxAAAAAIA1qVao+corr1RZ3myzzbL11ltn8803Xy9NAQAAAAB8kmqFmtttt10eeuihPPTQQ5k/f35WrlxZZbvZmgAAAADAhlKtUPP888/PBRdckM6dO2ebbbZJRUXF+u4LAAAAAGCNqhVqXnfddbnlllvSr1+/9d0PAAAAAMBabVadnZYtW5Zu3bqt714AAAAAAD5VtULNk08+Obfffvv67gUAAAAA4FNV6+fn//znP3PDDTfkwQcfzB577JE6depU2T5ixIj10hwAAAAAwKqqFWo+99xz6dixY5Jk+vTpVba5aRAAAAAAsCFVK9R8+OGH13cfAAAAAADrpFrX1NwQLr744lRUVGTQoEHldaVSKUOHDk2rVq1Sv3799OzZMy+88EKV/ZYuXZqBAwemWbNmadCgQfr06ZPXX3+9Ss2CBQvSr1+/VFZWprKyMv369cs777xTpWb27Nk59NBD06BBgzRr1iynnXZali1btqFOFwAAAACops9FqPnkk0/mhhtuyB577FFl/WWX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61VqFixYkH79+qWysjKVlZXp169f3nnnnSo1s2fPzqGHHpoGDRqkWbNmOe2007Js2bINcu4AAAAAQPXUaKg5YcKE/OhHP8oTTzyR8ePH54MPPsgBBxyQd999t1xz2WWXZcSIEbnmmmvy5JNPpmXLltl///2zePHics2gQYNy1113ZcyYMZk4cWKWLFmSQw45JCtWrCjX9O3bN9OmTcvYsWMzduzYTJs2Lf369StvX7FiRQ4++OC8++67mThxYsaMGZM777wzgwcP3jgvBgAAAACwTmrX5JOPHTu2yvLNN9+c5s2bZ+rUqdlnn31SKpVy1VVX5ZxzzsmRRx6ZJBk1alRatGiR22+/PaecckoWLlyYm266Kbfeemv222+/JMno0aPTunXrPPjgg+ndu3dmzJiRsWPH5oknnkiXLl2SJCNHjkzXrl0zc+bM7LLLLhk3blxefPHFzJkzJ61atUqSDB8+PCeccEIuuuiiNGrUaCO+MgAAAADAJ/lcXVNz4cKFSZImTZokSV555ZXMmzcvBxxwQLmmXr166dGjRx5//PEkydSpU7N8+fIqNa1atUq7du3KNZMmTUplZWU50EySvffeO5WVlVVq2rVrVw40k6R3795ZunRppk6dusZ+ly5dmkWLFlV5AAAAAAAb1ucm1CyVSjnjjDPy9a9/Pe3atUuSzJs3L0nSokWLKrUtWrQob5s3b17q1q2bxo0br7WmefPmqz1n8+bNq9Ss+jyNGzdO3bp1yzWruvjii8vX6KysrEzr1q0/62kDAAAAAJ/R5ybU/PGPf5znnnsuv/nNb1bbVlFRUWW5VCqttm5Vq9asqb46NR939tlnZ+HCheXHnDlz1toTAAAAAPDv+1yEmgMHDszvf//7PPzww/nSl75UXt+yZcskWW2m5Pz588uzKlu2bJlly5ZlwYIFa6154403VnveN998s0rNqs+zYMGCLF++fLUZnB+pV69eGjVqVOUBAAAAAGxYNRpqlkql/PjHP87vfve7/PGPf8z2229fZfv222+fli1bZvz48eV1y5Yty4QJE9KtW7ckSadOnVKnTp0qNXPnzs306dPLNV27ds3ChQszZcqUcs3kyZOzcOHCKjXTp0/P3LlzyzXjxo1LvXr10qlTp/V/8gAAAABAtdTo3c9/9KMf5fbbb88999yThg0blmdKVlZWpn79+qmoqMigQYMybNiwtG3bNm3bts2wYcOyxRZbpG/fvuXak046KYMHD07Tpk3TpEmTDBkyJO3bty/fDX233XbLgQcemP79++f6669PkvzgBz/IIYcckl122SVJcsABB2T33XdPv379cvnll+ftt9/OkCFD0r9/fzMwAQAAAOBzpEZDzWuvvTZJ0rNnzyrrb7755pxwwglJkrPOOivvv/9+BgwYkAULFqRLly4ZN25cGjZsWK6/8sorU7t27Rx11FF5//3306tXr9xyyy2pVatWuea2227LaaedVr5Lep8+fXLNNdeUt9eqVSv33XdfBgwYkO7du6d+/frp27dvrrjiig109gAAAABAddRoqFkqlT61pqKiIkOHDs3QoUM/sWbzzTfP1VdfnauvvvoTa5o0aZLRo0ev9bm+/OUv59577/3UngAAAACAmvO5uFEQAAAAAMC6EmoCAAAAAIUi1AQAAAAACkWoCQAAAAAUilATAAAAACgUoSYAAAAAUChCTQAAAACgUISaAAAAAEChCDUBAAAAgEIRagIAAAAAhSLUBAAAAAAKRagJAAAAABSKUBMAAAAAKBShJgAAAABQKEJNAAAAAKBQhJoAAAAAQKEINQEAAACAQhFqAgAAAACFItQEAAAAAApFqAkAAAAAFIpQEwAAAAAoFKEmAAAAAFAoQk0AAAAAoFCEmgAAAABAoQg1AQAAAIBCEWoCAAAAAIUi1AQAAAAACkWoCQAAAAAUilATAAAAACgUoSYAAAAAUChCTQAAAACgUISaAAAAAEChCDUBAAAAgEIRagIAAAAAhSLUBAAAAAAKRagJAAAAABSKUBMAAAAAKBShJgAAAABQKEJNAAAAAKBQhJoAAAAAQKEINQEAAACAQhFqAgAAAACFItQEAAAAAApFqAkAAAAAFIpQEwAAAAAoFKEmAAAAAFAoQk0AAAAAoFCEmgAAAABAoQg1AQAAAIBCEWoCAAAAAIUi1AQAAAAACkWoCQAAAAAUilATAAAAACgUoSYAAAAAUChCTQAAAACgUISaAAAAAEChCDUBAAAAgEIRagIAAAAAhSLUBAAAAAAKRagJAAAAABSKUBMAAAAAKBShJgAAAABQKEJNAAAAAKBQhJoAAAAAQKEINQEAAACAQhFqAgAAAACFItQEAAAAAApFqAkAAAAAFIpQEwAAAAAoFKHmKn71q19l++23z+abb55OnTrl0UcfremWAAAAAICPEWp+zB133JFBgwblnHPOyTPPPJNvfOMb+da3vpXZs2fXdGsAAAAAwP8Qan7MiBEjctJJJ+Xkk0/ObrvtlquuuiqtW7fOtddeW9OtAQAAAAD/o3ZNN/B5sWzZskydOjU/+9nPqqw/4IAD8vjjj69xn6VLl2bp0qXl5YULFyZJFi1atE7Pufj996vZLZ9FvXUcj+pY/P7yDXZs/mVd31Of1Xvvf7BBjsvqNtQY/vM9Y7gxbKjxS5IP3lu2wY7Nv2zIMVz+nr/PbAwbagyXv/feBjkuVW3Y9+CSDXZs/mVDjuF77y3eYMfmXxYtqrtBjrvkfeO3sSxaVH+DHHfxP32Obgz1P8Pn6EefuaVSaa11FaVPq9hE/P3vf8+2226bxx57LN26dSuvHzZsWEaNGpWZM2euts/QoUNz/vnnb8w2AQAAAOALb86cOfnSl770idvN1FxFRUVFleVSqbTauo+cffbZOeOMM8rLK1euzNtvv52mTZt+4j5FtmjRorRu3Tpz5sxJo0aNarodqsEYFpvxKz5jWHzGsPiMYbEZv+IzhsVnDIvPGBbbpjB+pVIpixcvTqtWrdZaJ9T8H82aNUutWrUyb968Kuvnz5+fFi1arHGfevXqpV69elXWbbXVVhuqxc+NRo0afWHfOJsKY1hsxq/4jGHxGcPiM4bFZvyKzxgWnzEsPmNYbF/08ausrPzUGjcK+h9169ZNp06dMn78+Crrx48fX+Xn6AAAAABAzTJT82POOOOM9OvXL507d07Xrl1zww03ZPbs2Tn11FNrujUAAAAA4H8INT/mu9/9bt56661ccMEFmTt3btq1a5f7778/2223XU239rlQr169nHfeeav95J7iMIbFZvyKzxgWnzEsPmNYbMav+Ixh8RnD4jOGxWb8/sXdzwEAAACAQnFNTQAAAACgUISaAAAAAEChCDUBAAAAgEIRarJeDR06NB07diwvn3DCCTn88MNrrB8osp49e2bQoEE13Qafgc+84vqsY1dRUZG77757g/VD9Xkf8klW/XsqAFBs7n7OejVkyJAMHDiwpttgIznhhBPyzjvv+GIP/+OXv/xl3H+vmIzdF4exBIDq8f2OohFqsl6USqWsWLEiW265ZbbccsuabgegRlRWVtZ0C1STsfviMJabpmXLlqVu3bo13QYAsBH5+fkmauzYsfn617+erbbaKk2bNs0hhxySWbNmJUleffXVVFRUZMyYMenWrVs233zzfOUrX8kjjzxS3v+RRx5JRUVF/vCHP6Rz586pV69eHn30UT/rWY/WNkYfvf7vvPNOuX7atGmpqKjIq6++Wl43cuTItG7dOltssUWOOOKIjBgxIltttVV5+5p+ojdo0KD07NmzvPzf//3fad++ferXr5+mTZtmv/32y7vvvpuhQ4dm1KhRueeee1JRUZGKiooq/x/hs3n33Xdz3HHHZcstt8w222yT4cOHV9m+bNmynHXWWdl2223ToEGDdOnSZbXX+7HHHkuPHj2yxRZbpHHjxundu3cWLFiwEc+Cj7+n1vYeTv71Wfu73/0u++67b7bYYot06NAhkyZNqqHuN20fH7s2bdrkqquuqrK9Y8eOGTp06Br3/eY3v5kf//jHVda99dZbqVevXv74xz9ugG5Zm886lhUVFbnxxhtzxBFHZIsttkjbtm3z+9//fuM1vAno2bNnBg4cmEGDBqVx48Zp0aJFbrjhhrz77rv5/ve/n4YNG2bHHXfMAw88kCRZsWJFTjrppGy//fapX79+dtlll/zyl7+scsyPxvniiy9Oq1atsvPOOydJXn/99Rx99NFp0qRJGjRokM6dO2fy5MlV9r311lvTpk2bVFZW5uijj87ixYs3zgvxBbS+x/ZPf/pT6tSpk3nz5lV5nsGDB2efffbZqOe2qenZs2dOO+20nHXWWWnSpElatmxZ5bNy9uzZOeyww7LlllumUaNGOeqoo/LGG28kSWbOnJmKioq89NJLVY45YsSItGnTxuz5jWzp0qU57bTT0rx582y++eb5+te/nieffLK8/YUXXsjBBx+cRo0apWHDhvnGN76RWbNm+X73OfFJ37+T5Oabb85uu+2WzTffPLvuumt+9atflfdblxzni0iouYl69913c8YZZ+TJJ5/MQw89lM022yxHHHFEVq5cWa4588wzM3jw4DzzzDPp1q1b+vTpk7feeqvKcc4666xcfPHFmTFjRvbYY4+NfRpfaOsyRmvz2GOP5dRTT81PfvKTTJs2Lfvvv38uuuiiz9TD3Llzc8wxx+TEE0/MjBkz8sgjj+TII49MqVTKkCFDctRRR+XAAw/M3LlzM3fu3HTr1q06p0o+fL89/PDDueuuuzJu3Lg88sgjmTp1ann797///Tz22GMZM2ZMnnvuuXznO9/JgQcemD//+c9JPgy1e/Xqla985SuZNGlSJk6cmEMPPTQrVqyoqVPa5K3re/icc87JkCFDMm3atOy888455phj8sEHH9RQ11THySefnNtvvz1Lly4tr7vtttvSqlWr7LvvvjXYGevq/PPPz1FHHZXnnnsuBx10UI499ti8/fbbNd3WF8qoUaPSrFmzTJkyJQMHDswPf/jDfOc730m3bt3y9NNPp3fv3unXr1/ee++9rFy5Ml/60pfy29/+Ni+++GJ+8Ytf5H//7/+d3/72t1WO+dBDD2XGjBkZP3587r333ixZsiQ9evTI3//+9/z+97/Ps88+m7POOqvK5+6sWbNy991359577829996bCRMm5JJLLtnYL8cXyvoc23322Sc77LBDbr311vLxP/jgg4wePTrf//73a+oUNxmjRo1KgwYNMnny5Fx22WW54IILMn78+JRKpRx++OF5++23M2HChIwfPz6zZs3Kd7/73STJLrvskk6dOuW2226rcrzbb789ffv2TUVFRU2czibrrLPOyp133plRo0bl6aefzk477ZTevXvn7bffzt/+9rfss88+2XzzzfPHP/4xU6dOzYknnpgPPvjA97vPgbV9/x45cmTOOeecXHTRRZkxY0aGDRuWn//85xk1alSVY6xLjvOFUoJSqTR//vxSktLzzz9feuWVV0pJSpdcckl5+/Lly0tf+tKXSpdeemmpVCqVHn744VKS0t13313lOOedd16pQ4cO5eXjjz++dNhhh22MU/jC+/gYffT6L1iwoLz9mWeeKSUpvfLKK6VSqVT67ne/Wzr44IOrHOPYY48tVVZWlpfXND4/+clPSj169CiVSqXS1KlTS0lKr7766hp7Mr7rx+LFi0t169YtjRkzprzurbfeKtWvX7/0k5/8pPSXv/ylVFFRUfrb3/5WZb9evXqVzj777FKpVCodc8wxpe7du2/Uvlnd2t4TH38Pl0ql8mftjTfeWK554YUXSklKM2bM2Bjt8jEfH7vtttuudOWVV1bZ3qFDh9J5551XXk5Suuuuu0qlUqn0z3/+s9SkSZPSHXfcUd7esWPH0tChQzdw16xJdcby3HPPLS8vWbKkVFFRUXrggQc2Qrebhh49epS+/vWvl5c/+OCDUoMGDUr9+vUrr5s7d24pSWnSpElrPMaAAQNK3/72t8vLxx9/fKlFixalpUuXltddf/31pYYNG5beeuutNR7jvPPOK22xxRalRYsWldedeeaZpS5dulT73DZ1G2JsL7300tJuu+1WXr777rtLW265ZWnJkiUb4Az4yKpjWSqVSnvttVfppz/9aWncuHGlWrVqlWbPnl3e9tHfWaZMmVIqlUqlESNGlHbYYYfy9pkzZ5aSlF544YWNcwKUSqUP/xtWp06d0m233VZet2zZslKrVq1Kl112Wenss88ubb/99qVly5atcX/f72rW2r5/t27dunT77bdXWfcf//Efpa5du5ZKpdI65ThfRGZqbqJmzZqVvn37ZocddkijRo2y/fbbJ/nwZwUf6dq1a/nPtWvXTufOnTNjxowqx+ncufPGaXgTtC5jtDYzZ87M1772tSrrVl3+NB06dEivXr3Svn37fOc738nIkSP9nHkDmDVrVpYtW1blPdekSZPssssuSZKnn346pVIpO++8c/m6tVtuuWUmTJhQ/jnzRzM1+fxY1/fwx2e5b7PNNkmS+fPnb7xG+bfVq1cv3/ve9/LrX/86yYfvx2effTYnnHBCzTbGOvv4+7BBgwZp2LCh9+F69vHXuFatWmnatGnat29fXteiRYsk//r8u+6669K5c+dsvfXW2XLLLTNy5MjVPj/bt29f5Tqa06ZNy5577pkmTZp8Yh9t2rRJw4YNy8vbbLONsf43re+xPeGEE/KXv/wlTzzxRJLk17/+dY466qg0aNBgY5zOJm3VX9599P6YMWNGWrdundatW5e37b777tlqq63K3w+PPvrovPbaa+Vxu+2229KxY8fsvvvuG+8EyKxZs7J8+fJ07969vK5OnTr52te+lhkzZmTatGn5xje+kTp16tRgl3yST/r+/eabb2bOnDk56aSTqnwfvPDCC6tc3ipZtxzni8SNgjZRhx56aFq3bp2RI0emVatWWblyZdq1a5dly5atdb9VfzrgLxcbztrG6KObMZU+dn2a5cuXV9m/VCqtNl6lVa5ns9lmm6227uPHqVWrVsaPH5/HH38848aNy9VXX51zzjknkydPLgc0/PtWHYNVrVy5MrVq1crUqVNTq1atKts++v9C/fr1N1h/VM+6fs5+/C+VH71n1/UyE2wYn/bZuCYnn3xyOnbsmNdffz2//vWv06tXr2y33XYbsk3WwbqO5apf7ioqKrwP17M1vcaf9Pn329/+NqeffnqGDx+erl27pmHDhrn88stXuzbmqn8PXZf/Fhrr9W99j23z5s1z6KGH5uabb84OO+yQ+++//wt/TbjPi096f6zpe0VS9fvGNttsk3333Te333579t577/zmN7/JKaecslH65l8++m/emr4HVlRU+M7wOfdJ37//3//7f0k+vGdGly5dVtvn03yRLwFhpuYm6K233sqMGTNy7rnnplevXtltt93WOPvuo39lSz68ls3UqVOz6667bsxWN1mfNkZbb711kg+vufGRadOmVTnGrrvumilTplRZ99RTT1VZ3nrrrascY03HqaioSPfu3XP++efnmWeeSd26dXPXXXclSerWreuajevBTjvtlDp16lR5zy1YsCAvv/xykmTPPffMihUrMn/+/Oy0005VHi1btkzy4b+sP/TQQzXSP6tb189ZPp9W/WxctGhRXnnllbXu0759+3Tu3DkjR47M7bffnhNPPHFDt8k6qM5YUvMeffTRdOvWLQMGDMiee+6ZnXbaabWZKGuyxx57ZNq0aa6H+jm2rmN78sknZ8yYMbn++uuz4447Vpl1xsa3++67Z/bs2ZkzZ0553YsvvpiFCxdmt912K6879thjc8cdd2TSpEmZNWtWjj766Jpod5O20047pW7dupk4cWJ53fLly/PUU09lt912yx577JFHH330E/+x1ve7mrem79+PPfZYtt122/z1r39d7fvgqpONNrUcR6i5CWrcuHGaNm2aG264IX/5y1/yxz/+MWecccZqdf/n//yf3HXXXXnppZfyox/9KAsWLPAlbSP5tDHaaaed0rp16wwdOjQvv/xy7rvvvtXulj1w4MDcf//9GTFiRP785z/n+uuvzwMPPFDlX2m++c1v5qmnnsp//dd/5c9//nPOO++8TJ8+vbx98uTJGTZsWJ566qnMnj07v/vd7/Lmm2+W//LSpk2bPPfcc5k5c2b+8Y9/fOpMJtZsyy23zEknnZQzzzwzDz30UKZPn54TTjghm2324Uf0zjvvnGOPPTbHHXdcfve73+WVV17Jk08+mUsvvTT3339/kuTss8/Ok08+mQEDBuS5557LSy+9lGuvvTb/+Mc/avLUNlnr+jnL59M3v/nN3HrrrXn00Uczffr0HH/88ev0r+Ann3xyLrnkkqxYsSJHHHHERuiUT1PdsaRm7bTTTnnqqafyhz/8IS+//HJ+/vOfV7lz7yc55phj0rJlyxx++OF57LHH8te//jV33nlnJk2atBG6Zl2s69j27t07lZWVufDCC90g6HNgv/32yx577JFjjz02Tz/9dKZMmZLjjjsuPXr0qHI5siOPPDKLFi3KD3/4w+y7777Zdttta7DrTVODBg3ywx/+MGeeeWbGjh2bF198Mf379897772Xk046KT/+8Y+zaNGiHH300Xnqqafy5z//ObfeemtmzpyZxPe7mra2799Dhw7NxRdfnF/+8pd5+eWX8/zzz+fmm2/OiBEjqhxjU8txhJqboM022yxjxozJ1KlT065du5x++um5/PLLV6u75JJLcumll6ZDhw559NFHc88996RZs2Y10PGm59PGqE6dOvnNb36Tl156KR06dMill16aCy+8sMoxunfvnuuuuy4jRoxIhw4dMnbs2Jx++unZfPPNyzW9e/fOz3/+85x11lnZa6+9snjx4hx33HHl7Y0aNcqf/vSnHHTQQdl5551z7rnnZvjw4fnWt76VJOnfv3922WWX8nWRHnvssQ38ynxxXX755dlnn33Sp0+f7Lfffvn617+eTp06lbfffPPNOe644zJ48ODssssu6dOnTyZPnly+ttHOO++ccePG5dlnn83Xvva1dO3aNffcc09q13aVkZqwrp+zfD6dffbZ2WeffXLIIYfkoIMOyuGHH54dd9zxU/c75phjUrt27fTt27fKZy01p7pjSc069dRTc+SRR+a73/1uunTpkrfeeisDBgz41P3q1q2bcePGpXnz5jnooIPSvn37XHLJJYLsz5F1HdvNNtssJ5xwQlasWFHl76bUjIqKitx9991p3Lhx9tlnn+y3337ZYYcdcscdd1Spa9SoUQ499NA8++yzOfbYY2uoWy655JJ8+9vfTr9+/fLVr341f/nLX/KHP/yh/I/uf/zjH7NkyZL06NEjnTp1ysiRI8uXHvD9rmat7fv3ySefnBtvvDG33HJL2rdvnx49euSWW25ZbabmppbjVJQ+7WJubHJeffXVbL/99nnmmWfSsWPHmm6H9ah///556aWX8uijj9Z0K/CFdMwxx6RWrVoZPXp0TbfCZ7Q+xm7OnDlp06ZNnnzyyXz1q19dj93xWXgfwhdD//7988Ybb+T3v/99TbcC8Lm3qeY4ZmrCF9gVV1yRZ599Nn/5y19y9dVXZ9SoUTn++ONrui34wvnggw/y4osvZtKkSfnKV75S0+3wGayPsVu+fHlmz56dn/70p9l7770FmjXE+xC+GBYuXJgHH3wwt912WwYOHFjT7QDwOSbUhC+wKVOmZP/990/79u1z3XXX5T//8z9z8skn13Rb8IUzffr0dO7cOV/5yldy6qmn1nQ7fAbrY+wee+yxbLfddpk6dWquu+669dwh68r7EL4YDjvssPTp0yennHJK9t9//5puB4DPMT8/BwAAAAAKxUxNAAAAAKBQhJoAAAAAQKEINQEAAACAQhFqAgAAAACFItQEAOALbejQoenYsWNNtwEAwHok1AQA4AujoqIid999d023AQDABibUBAAAAAAKRagJAMB617NnzwwcODCDBg1K48aN06JFi9xwww1599138/3vfz8NGzbMjjvumAceeKC8z4QJE/K1r30t9erVyzbbbJOf/exn+eCDD6oc87TTTstZZ52VJk2apGXLlhk6dGh5e5s2bZIkRxxxRCoqKsrLH7n11lvTpk2bVFZW5uijj87ixYvX+VzW9rxJsnDhwvzgBz9I8+bN06hRo3zzm9/Ms88+W95Wq1atTJ06NUlSKpXSpEmT7LXXXuX9f/Ob32SbbbZZp34AABBqAgCwgYwaNSrNmjXLlClTMnDgwPzwhz/Md77znXTr1i1PP/10evfunX79+uW9997L3/72txx00EHZa6+98uyzz+baa6/NTTfdlAsvvHC1YzZo0CCTJ0/OZZddlgsuuCDjx49Pkjz55JNJkptvvjlz584tLyfJrFmzcvfdd+fee+/NvffemwkTJuSSSy75TOfySc9bKpVy8MEHZ968ebn//vszderUfPWrX02vXr3y9ttvp7KyMh07dswjjzySJHnuuefK/7to0aIkySOPPJIePXpU74UGANgECTUBANggOnTokHPPPTdt27bN2Wefnfr166dZs2bp379/2rZtm1/84hd566238txzz+VXv/pVWrdunWuuuSa77rprDj/88Jx//vkZPnx4Vq5cWT7mHnvskfPOOy9t27bNcccdl86dO+ehhx5Kkmy99dZJkq222iotW7YsLyfJypUrc8stt6Rdu3b5xje+kX79+pX3Wxdre96HH344zz//fP7v//2/6dy5c9q2bZsrrrgiW221Vf77v/87yYezPT8KNR955JH06tUr7dq1y8SJE8vrevbsWe3XGgBgUyPUBABgg9hjjz3Kf65Vq1aaNm2a9u3bl9e1aNEiSTJ//vzMmDEjXbt2TUVFRXl79+7ds2TJkrz++utrPGaSbLPNNpk/f/6n9tKmTZs0bNjwM++3Ls87derULFmyJE2bNs2WW25ZfrzyyiuZNWtWkg9DzUcffTQrV67MhAkT0rNnz/Ts2TMTJkzIvHnz8vLLL5upCQDwGdSu6QYAAPhiqlOnTpXlioqKKus+CjBXrlyZUqlUJdBMPvxZ98frPumYH5/J+Vl6WZf91mX/lStXZptttinPxPy4rbbaKkmyzz77ZPHixXn66afz6KOP5j/+4z/SunXrDBs2LB07dkzz5s2z2267rXM/AACbOqEmAAA1bvfdd8+dd95ZJdx8/PHH07Bhw2y77bbrfJw6depkxYoVG6rNNfrqV7+aefPmpXbt2qvdnOgjH11X85prrklFRUV23333tGrVKs8880zuvfdeszQBAD4jPz8HAKDGDRgwIHPmzMnAgQPz0ksv5Z577sl5552XM844I5tttu5/ZW3Tpk0eeuihzJs3LwsWLNiAHf/Lfvvtl65du+bwww/PH/7wh7z66qt5/PHHc+655+app54q1/Xs2TOjR49Ojx49UlFRkcaNG2f33XfPHXfc4XqaAACfkVATAIAat+222+b+++/PlClT0qFDh5x66qk56aSTcu65536m4wwfPjzjx49P69ats+eee26gbquqqKjI/fffn3322Scnnnhidt555xx99NF59dVXy9cNTZJ99903K1asqBJg9ujRIytWrDBTEwDgM6oofXSxIgAAAACAAjBTEwAAAAAoFKEmAACbrNmzZ2fLLbf8xMfs2bNrukUAANbAz88BANhkffDBB3n11Vc/cXubNm1Su3btjdcQAADrRKgJAAAAABSKn58DAAAAAIUi1AQAAAAACkWoCQAAAAAUilATAAAAACgUoSYAAAAAUChCTQAAAACgUISaAAAAAEChCDUBAAAAgEL5//ktc2jLT9hCAAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 1600x500 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(16,5))\n",
    "sns.barplot(x=\"month_new\",y=\"number\",data=data1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "35fa7ec7-68c4-46b4-801f-11dbe59baa54",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>year</th>\n",
       "      <th>number</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1998</td>\n",
       "      <td>20013.971</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1999</td>\n",
       "      <td>26882.821</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2000</td>\n",
       "      <td>27351.251</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2001</td>\n",
       "      <td>29054.612</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2002</td>\n",
       "      <td>37390.600</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>2003</td>\n",
       "      <td>42760.674</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>2004</td>\n",
       "      <td>38450.163</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>2005</td>\n",
       "      <td>35004.965</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>2006</td>\n",
       "      <td>33824.161</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>2007</td>\n",
       "      <td>33028.413</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>2008</td>\n",
       "      <td>29378.964</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>2009</td>\n",
       "      <td>39116.178</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>2010</td>\n",
       "      <td>37037.449</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>2011</td>\n",
       "      <td>34633.545</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>2012</td>\n",
       "      <td>40084.860</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>2013</td>\n",
       "      <td>35137.118</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>2014</td>\n",
       "      <td>39621.183</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>2015</td>\n",
       "      <td>41208.292</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>2016</td>\n",
       "      <td>42212.229</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>2017</td>\n",
       "      <td>36619.624</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    year     number\n",
       "0   1998  20013.971\n",
       "1   1999  26882.821\n",
       "2   2000  27351.251\n",
       "3   2001  29054.612\n",
       "4   2002  37390.600\n",
       "5   2003  42760.674\n",
       "6   2004  38450.163\n",
       "7   2005  35004.965\n",
       "8   2006  33824.161\n",
       "9   2007  33028.413\n",
       "10  2008  29378.964\n",
       "11  2009  39116.178\n",
       "12  2010  37037.449\n",
       "13  2011  34633.545\n",
       "14  2012  40084.860\n",
       "15  2013  35137.118\n",
       "16  2014  39621.183\n",
       "17  2015  41208.292\n",
       "18  2016  42212.229\n",
       "19  2017  36619.624"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data2=data.groupby('year')['number'].sum().reset_index()\n",
    "data2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "6654be13-6df8-4b8e-95f8-72c46734b3a3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: xlabel='year', ylabel='number'>"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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qtra2lbrHQAAAAAAAEDT+DXUvOGGG/T888/r448/1scff6w77rhDd911l3bv3m3WjBw5UmVlZea2bt06r3NMmzZNq1evVm5urgoKClRdXa3U1FTV19ebNenp6SopKZHL5ZLL5VJJSYmcTqd5vL6+XqNHj1ZNTY0KCgqUm5urVatWacaMGa3/JgAAAAAAAAC4Ih39+eJjxozxejx79mwtXrxYRUVF+uEPfyhJstvtio6OvuDz3W63li1bphUrVmj48OGSpJycHMXFxWnDhg1KSUnR3r175XK5VFRUpAEDBkiSli5dqqSkJO3bt0/x8fHKy8vTnj17VFpaqtjYWEnS/PnzNXHiRM2ePVthYWGt9RYAAAAAAAAAuEJ+DTXPVV9frz/84Q+qqalRUlKSuX/z5s2KjIzUtddeqyFDhmj27NmKjIyUJBUXF6uurk7JyclmfWxsrBISErR161alpKSosLBQDofDDDQlaeDAgXI4HNq6davi4+NVWFiohIQEM9CUpJSUFHk8HhUXF2vYsGE+eAcAAAAAAGg5f37nW38PodlG3Rfh7yEAaKP8Hmru3LlTSUlJOnXqlK655hqtXr1avXv3liSNGjVK9957r7p37679+/frN7/5je644w4VFxfLbrervLxcgYGB6tKli9c5o6KiVF5eLkkqLy83Q9BzRUZGetVERUV5He/SpYsCAwPNmgvxeDzyeDzm46qqqqa9CQAAAAAAAAAaze+hZnx8vEpKSnT8+HGtWrVKEyZM0JYtW9S7d2/dd999Zl1CQoL69++v7t27a+3atRo3btxFz2kYhmw2m/n43D83p+Z8c+fO1bPPPnvZHgEAsLpR793j7yE025/vWuXvIQAAAABoIX69UZAkBQYG6qabblL//v01d+5c9evXT6+88soFa2NiYtS9e3d9/vnnkqTo6GjV1taqsrLSq66iosJceRkdHa3Dhw83ONeRI0e8as5fkVlZWam6uroGKzjPNWvWLLndbnMrLS1tfOMAAAAAAAAAmsTvoeb5DMPw+kr3uY4eParS0lLFxMRIkhITE9WpUyfl5+ebNWVlZdq1a5cGDRokSUpKSpLb7dZHH31k1mzbtk1ut9urZteuXSorKzNr8vLyZLfblZiYeNGx2u12hYWFeW0AAAAAAAAAWpdfv37+5JNPatSoUYqLi9OJEyeUm5urzZs3y+Vy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ED3xxBP67rvvVFNTo1//+tc6c+aMWWOz2ZSfn68dO3YoNDRUQUFBWrhwoVwul9+vYXMhLdX3HXfcofLycr344ouqra1VZWWluWz6bI0/GYah6dOn6yc/+YkSEhIkyfxqWVRUlFdtVFSUeay8vFyBgYHq0qXLJWsiIyMbvGZkZKTfLjlwVmv23Zb5su8vv/xS2dnZeuSRR1q6jSvmi76feOIJhYSEqGvXrjp48KDee++91mqn0Vqzb8MwNHHiRD3yyCN++RrupbT25/2rX/1Kubm52rRpkx5//HG9/PLLmjx5cmu21Cit2fff//53SVJWVpaefvpprVmzRl26dNGQIUN07NixVu3rcnz599qyZcuUkpKiuLi4lm7jirVm3215ztaafbflOVtT+26M9jhfszpf9t0e5mtXoj3N1xp77vY2X2us9jZfa4z2OF9rCl/O1wg1LaBTp05atWqVPvvsM4WHh6tz587avHmzRo0apYCAAEnSddddpz/84Q/64IMPdM0118jhcMjtdutHP/qRWWMYhiZPnqzIyEj9z//8jz766CPdddddSk1N9ftE8UJaqu8f/vCHevPNNzV//nx17txZ0dHRuvHGGxUVFWXW+NPjjz+uTz/9VP/93//d4JjNZvN6bBhGg33nO7/mQvWNOU9ra+2+2ypf9f3NN99o5MiRuvfee/Xggw82b9AtwBd9//rXv9aOHTuUl5engIAA/eIXv5BhGM0ffDO0Zt/Z2dmqqqrSrFmzWm7ALaS1P+9/+7d/05AhQ9S3b189+OCDevXVV7Vs2TIdPXq0ZRpootbs++x1op966indc889SkxM1BtvvCGbzaY//OEPLdRB0/jq77VDhw5p/fr1mjRpUvMG3EJas++2PGdrzb7b8pytpfu+3Dmaep6W1tp9t1W+6ru9z9cu5GqYr53rapqvne9qma+d62qar12Mr+drhJoWkZiYqJKSEh0/flxlZWVyuVw6evSoevToYdYkJyfryy+/VEVFhb799lutWLFCX3/9tVmzceNGrVmzRrm5uRo8eLB+9KMf6T//8z8VHBysN99801+tXVJL9C394+Lr5eXl+vrrr3X06FFlZWXpyJEjXjX+MGXKFL3//vvatGmTbrjhBnN/dHS0JDX4vyMVFRXm/0WJjo42VzFcqub8O8FL0pEjRxr83xhfau2+2ypf9f3NN99o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evPNN7Vx40bNnDnT63W+++47zZ07V6+//rp2796tyMhIn/UIAACAi7MZhmH4exAAAADAlZo8ebK++uorrVu3TpL0yiuv6He/+52++OILDRkyRKNGjdKsWbPM+pycHM2cOVPffPPNBc/3hz/8QY8++qi+/fZbSf9YqfnLX/5SJSUl6tevX+s3BAAAgEYj1AQAAIAl7dixQ7fddpsOHDig66+/Xrfccovuuece/eY3v1FISIjOnDmjgIAAs76+vl6nTp1STU2NOnfurE2bNmnOnDnas2ePqqqqdPr0aZ06dUrV1dUKCQnR8uXL9fDDD+vUqVOy2Wx+7BQAAADn6+jvAQAAAABNceutt6pfv3566623lJKSop07d+qDDz6QJJ05c0bPPvusxo0b1+B5QUFBOnDggH7605/qkUce0X/8x38oPDxcBQUFmjRpkurq6sza4OBgAk0AAIA2iFATAAAAlvXggw9q4cKF+vrrrzV8+HDFxcVJkn70ox9p3759uummmy74vI8//linT5/W/Pnz1aHDPy4z//vf/95n4wYAAEDzEGoCAADAsh544AFlZmZq6dKleuutt8z9//f//l+lpqYqLi5O9957rzp06KBPP/1UO3fu1HPPPafvf//7On36tLKzszVmzBj99a9/1auvvurHTgAAAHAluPs5AAAALCssLEz33HOPrrnmGo0dO9bcn5KSojVr1ig/P1+33XabBg4cqAULFqh79+6SpFtuuUULFizQCy+8oISEBK1cuVJz5871UxcAAAC4UtwoCAAAAJY2YsQI9erVS7/73e/8PRQAAAD4CKEmAAAALOnYsWPKy8vTAw88oD179ig+Pt7fQwIAAICPcE1NAAAAWNKPfvQjVVZW6oUXXiDQBAAAuMqwUhMAAAAAAACApXCjIAAAAAAAAACWQqgJAAAAAAAAwFIINQEAAAAAAABYCqEmAAAAAAAAAEsh1AQAAAAAAABgKYSaAAAAAAAAACyFUBMAAAAAAACApRBqAgAAAAAAALAUQk0AAAAAAAAAlvL/AVwL1mAVJNU7AAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 1600x500 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(16,5))\n",
    "sns.barplot(x=\"year\",y=\"number\",data=data2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "fe4e8736-ab05-455f-9ea9-03abd39f4482",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['year', 'state', 'month', 'number', 'date', 'month_new'], dtype='object')"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "ff4e9c3c-877b-42c2-b768-b4af3c5502e4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>state</th>\n",
       "      <th>number</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Acre</td>\n",
       "      <td>18464.030</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Alagoas</td>\n",
       "      <td>4606.000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Amapa</td>\n",
       "      <td>21831.576</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Amazonas</td>\n",
       "      <td>30650.129</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Bahia</td>\n",
       "      <td>44746.226</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Ceara</td>\n",
       "      <td>30428.063</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Distrito Federal</td>\n",
       "      <td>3561.000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Espirito Santo</td>\n",
       "      <td>6546.000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Goias</td>\n",
       "      <td>37695.520</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>Maranhao</td>\n",
       "      <td>25129.131</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>Mato Grosso</td>\n",
       "      <td>96246.028</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>Minas Gerais</td>\n",
       "      <td>37475.258</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>Paraiba</td>\n",
       "      <td>52426.918</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>Pará</td>\n",
       "      <td>24512.144</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>Pernambuco</td>\n",
       "      <td>24498.000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>Piau</td>\n",
       "      <td>37803.747</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>Rio</td>\n",
       "      <td>45094.865</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>Rondonia</td>\n",
       "      <td>20285.429</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>Roraima</td>\n",
       "      <td>24385.074</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>Santa Catarina</td>\n",
       "      <td>24359.852</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20</th>\n",
       "      <td>Sao Paulo</td>\n",
       "      <td>51121.198</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21</th>\n",
       "      <td>Sergipe</td>\n",
       "      <td>3237.000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>22</th>\n",
       "      <td>Tocantins</td>\n",
       "      <td>33707.885</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               state     number\n",
       "0               Acre  18464.030\n",
       "1            Alagoas   4606.000\n",
       "2              Amapa  21831.576\n",
       "3           Amazonas  30650.129\n",
       "4              Bahia  44746.226\n",
       "5              Ceara  30428.063\n",
       "6   Distrito Federal   3561.000\n",
       "7     Espirito Santo   6546.000\n",
       "8              Goias  37695.520\n",
       "9           Maranhao  25129.131\n",
       "10       Mato Grosso  96246.028\n",
       "11      Minas Gerais  37475.258\n",
       "12           Paraiba  52426.918\n",
       "13              Pará  24512.144\n",
       "14        Pernambuco  24498.000\n",
       "15              Piau  37803.747\n",
       "16               Rio  45094.865\n",
       "17          Rondonia  20285.429\n",
       "18           Roraima  24385.074\n",
       "19    Santa Catarina  24359.852\n",
       "20         Sao Paulo  51121.198\n",
       "21           Sergipe   3237.000\n",
       "22         Tocantins  33707.885"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data3=data.groupby('state')['number'].sum().reset_index()\n",
    "data3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "cda1302c-d9bd-4c37-aae3-86fd8b864f9f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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ES9LPProo1qxYoUqVKigVq1aqVevXlq1apVWrFihJ554wux4bklNTdXKlSuduz2uXLnSWdAcOXJE0dHRGjlypGUv8ZSy/6U/96pfv37q2bOntm/frjp16jivuJg9e7bef/99s+O5LTo6WsuXL8/wRqN06dIZLj22mlq1amndunUKDw9Xs2bN1K9fP+3atUuLFi1SrVq1zI53z+xepE2dOlV9+vTRv/71L+cmHhs3blTTpk01YcIEde/e3eSE96Zdu3YZjr388ssmJMHdsuvzvGS/TSInT56sN998U+3atdO3336rDh066ODBg9qyZYu6detmdjy3GIahwMBA+fr66tq1aypQoIB++OEHs2NlmRkzZujpp59WoUKFnFc5xcfHq0SJEvr2228lSRcuXLDUpJorV65kuHQ/u+FSd5tLS0vT999/r1mzZlm2+HzggQe0dOlS1a9f3+X4zz//rKeeekrnz5/XoUOH9PDDD1tmA4zAwED98MMPqlu3rtlRslRwcLDmzZuXoYRevny52rZtq5MnT5qULGsMHjxYAQEB+ve//62FCxfqpZdeUrFixRQfH68+ffpozJgxZke8Z8nJyWratKn27Nmj8+fPKzQ0VAkJCapVq5Z+/PHHDLtDWsGECRP0888/a86cOc7dEM+ePasOHTro0UcfVb9+/UxO6J4zZ87o0qVLCg0NVXp6usaNG6e1a9eqVKlSGjJkSLbf+fF2PvnkEy1dulTff/+9pOuXPz700EPy8fGRJO3du1cDBw7MsM6YVVjh0h93LF68WOPHj3eu83Zjt9+WLVuanMx9/v7+2rZtm0qXLu2y7MeWLVvUpEkTnT592uyIbjt06JAuXLigihUr6uLFi+rfv7/zuWPixIkqWrSo2RHvyV9t5nGDVWcFPfjgg3rjjTcyFJwffPCBRo0apd9//92kZPgnsePzvB03iSxbtqyGDRuml156yeV319ChQ3XmzBlNnTrV7Ij35MiRI86lj6Trs48XLVpk+eXSbpWenq7o6Gjt379fhmGobNmyatSo0V2vE5/dDBo0SA888EC2LmspPpHttWnTRhs2bND48eNVvXp1ORwObd68Wf3791edOnU0b948zZ8/X+PGjdPWrVvNjntXwsPDNX/+fFWsWNHsKFmqZ8+eWrx4scaNG+fyCfGAAQP03HPPadKkSWZHzFKbNm3SunXrVKpUKUvuznyzVatWadu2bUpPT1eVKlUseTndDQ8++KCio6Odl3LesHv3bjVu3Jg3jdnIY489pj59+uiZZ56RJJcX7dL1nWU/+OADbdiwwcyYbitYsKDee++9bH3pz724du2aRo0apVdeecV2lzs2a9ZMVapU0VtvveVcf7Bo0aJ68cUXlZ6eroULF5od0S1paWlau3atKlasaMkPR/6J/P39FRsbm+Ey4wMHDqhy5cq6cOGCSckAa7PjJpG+vr6Ki4tT0aJFFRQUpBUrVqhSpUo6cOCAatWqZbkP7V544QVt375dw4YNU65cuTR27FilpaVp8+bNZkfLEteuXVOuXLm0ffv2DGt8WlmvXr00d+5cVaxYURUrVpSnp6fL49lhmTEudUe298knn6hPnz568cUXnes35cyZU+3atdPEiRMlXf+0a8aMGWbGvCfjx4/XoEGD9PHHH1tupsWdjBs3Tg6HQ23btnX+rDw9PfX6669bcjbkrU6fPq18+fJJur4Zy7Jly5SammrJy/hXrVql7t27a+PGjQoICNDjjz+uxx9/XJKUlJSkhx56SB9//LEeffRRk5Peu+TkZJ08eTJD8ZmYmOhcL8hK0tPTlZ6e7rKExMmTJ/Xxxx8rJSVFLVq00COPPGJiQvft379fZcqUcd7PlSuXy6fdNWrUsOylWpI1Lv25Fzlz5tTYsWNve+mq1Y0dO1b169fX1q1bdeXKFQ0cOFB79uzRmTNntG7dOrPjuc3Dw0MRERGKi4uj+LSIFi1aaPHixRowYIDL8W+//VZPPfWUSakA6zt48KCaNWsm6foGTikpKXI4HOrTp48ef/xxSxafISEhOn36tIoWLaqiRYtq48aNqlSpkg4fPiwrzm/773//qy+//FL16tWTdP11YNGiRZWamuq8GsjKcubMqaJFiyotLc3sKFlq586devjhhyXJOVv3huyypB/FJ7K9Bx54QNOnT9fEiRN16NAhGYahkiVL6oEHHnCOufEPzSqqVaumS5cuqUSJEvL19c3wqciZM2dMSpY5Xl5eev/99/XOO+/o4MGDMgxDpUqVkq+vr9nRMmXXrl166qmndOzYMZUuXVrz589XkyZNlJKSohw5cmjixIlauHChnn76abOj3rVJkyapU6dOLmvn3hAYGKjOnTtrwoQJliw+n3nmGXXo0EHjx493rl+3ceNGDRgw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14rat29vJCUlmR0D9yAgIMD47bffDMNwfS115MgRw9vb28xobrNCX8Ol7sj27LgD3w2rVq3SrFmztGjRIhUtWlTPPfecnnvuOVWuXNnsaIBlNWvWTFWqVNFbb70lf39/7dy5U0WLFtWLL76o9PR0LVy40OyI+IewwqU/dyskJEQrV67UQw89JEkqUKCAtmzZomLFikmS9u/fr+rVq1tuduSLL76oixcv6rvvvrvt482bN5efn5+++uqrvzlZ1ilYsKC+/fZb1ahRQwEBAdq6davKlCmj7777Tu+9957Wrl1rdkTcZM6cOYqKitKsWbOcM6qBv1t6erp+++23264z+9hjj5mUKnP+6qqfokWL/k1J8E8WHBysqKgoVa5c2WV5nejoaHXs2FHHjh0zO+I9s0Jfw6XuyPZuXufNDjvwHT9+XLNnz9asWbOUkpKiVq1a6erVq/rmm28UHh5udrws8euvv2ZYR8zhcOipp54yMRX+KcaOHav69etr69atunLligYOHKg9e/bozJkzrHWEv5UlLv25S0lJScqZ8/+/bDx16pTL4+np6S5rflrFoEGDVLt2bT3//PMaOHCgypQpI0nat2+f3n33Xf30009av369ySkzJyUlxbnjb968eXXq1CmVKVNGFSpU0LZt20xOh1s9//zz+vLLLxUUFKRixYpl2ACTnxnut40bN6p169Y6evSobp0jZeW9COxabNplLfE/Y9y0HJcdtGzZUiNHjtSCBQskXT+v+Ph4DR48WM8995zJ6dxjhb6G4hPZUnJy8l2PtdIO6E2bNtXatWvVvHlzTZkyRU2aNJGHh4c+/vhjs6NliUOHDumZZ57Rrl275HA4MvyisuoLJVhLeHi4du7cqQ8//FAeHh5KSUnRs88+q27dumWbnQXxz/Doo49qxYoVqlChglq1aqVevXpp1apVWrFihZ544gmz492TQoUKaffu3QoLC7vt4zt37sywrq4VVK5cWV999ZVeffXVDG8Q8+TJo/nz56tKlSompcsaYWFh2rdvn4oVK6aHH35Yn3zyiYoVK6aPP/6Y58RsqH379oqJidHLL798282NgPutS5cuqlatmpYtW6aCBQva6u/gwYMHNWnSJMXFxcnhcKhcuXLq1auXSpYsaXY0t9hpLfFbzZ07V2PHjtWBAwckSWXKlNGAAQMUGRlpcrLMGTdunJo2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fz9cXFyUr/v164dz586JiEaklnjUnYiItMKOHTuwePHiekVPABg1ahRCQkKwfft2AcmIiIiIiBpHx44dcebMGQDA3bt3UVBQgEGDBimv37hxA3p6eqLiEakdFj6JiEgrFBcXqzztfpyrqyuKioqaMBERERERUeNycXFBSEgIDhw4gEWLFsHQ0BDDhg1TXi8uLoaNjY3AhETqhUfdiYhIK1RVVakc+3lcx44dce3atSZMRERERETUuFavXg0vLy84OTnByMgIcXFx0NfXV16PiYnBuHHjBCYkUi8cbkRERFpBR0cHly5dQocOHZ54/fLly+jSpQvkcnkTJyMiIiIialw1NTUwMjKCjo6OynpVVRWMjIxUiqFEzRl3fBIRkVZQKBSYNm0aWrRo8cTrd+7caeJERERERESvh6mp6RPX27Zt28RJiNQbC59ERKQVPvroo+few4nuREREREREzQePuhMREREREREREZHW4VR3IiIiIiIiIiIi0josfBIREREREREREZHWYeGTiIiIiIiIiIiItA4Ln0RERERERERERKR1WPgkIiIiIiIiIiIircPCJxERERE1G9OmTYOnp+dLf92KFSvQp0+fRs9DRERERK8PC59ERERERERERESkdVj4JCIiIiKts2vXLtjb28PAwADt2rXDmDFjMH/+fMTFxeHHH3+ERCKBRCLBvn37AAALFy5Et27dYGhoCGtrayxbtgz37t0DAMTGxiIsLAxFRUXKr4uNjQUA1NTUYObMmTAzM4OJiQlGjRqFoqIiQe+aiIiIiB6lKzoAEREREVFjunjxIiZNmoTPPvsMEyZMwI0bN3DgwAFMnToVFRUVuH79OrZt2wYAaNu2LQDA2NgYsbGx6NKlC0pKSjBjxgwYGxtjwYIF8Pb2xq+//oqMjAz8/PPPAABTU1MoFAq4ubmhbdu2SE9Ph6mpKbZs2YLRo0fj1KlTyt+biIiIiMRg4ZOIiIiItMrFixdx//59eHl5QSaTAQDs7e0BAAYGBrhz5w46deqk8jVLly5V/trS0hJBQUHYuXMnFixYAAMDAxgZGUFXV1fl63JyclBSUoIrV66gRYsWAIB169YhNTUVu3btwsyZM1/3WyUiIiKiZ2Dhk4iIiIi0Su/evTF69GjY29vD2dkZ48aNw3vvvYc2bdo89Wt27dqF9evX4/Tp0/jzzz9x//59mJiYPPOfc/z4cfz5559o166dyvrt27fxxx9/NMp7ISIiIqKGY+GTiIiIiLSKjo4OsrKycOjQIWRmZmLjxo1YsmQJ8vPzn3j/kSNHMHHiRISFhcHZ2RmmpqZITExEZGTkM/85dXV16Ny5s7JP6KNat27dCO+EiIiIiF4FC59EREREpHUkEgmGDBmCIUOGYPny5ZDJZEhJSYG+vj7kcrnKvQcPHoRMJsOSJUuUa2fPnlW550lf17dvX1y6dAm6urqwtLR8be+FiIiIiBqGhU8iIiIi0ir5+fnIzs7GuHHjYGZmhvz8fPznP/9Bz549UVtbiz179uDkyZNo164dTE1NYWtri4qKCiQmJqJfv3745z//iZSUFJXf09LSEmfOnEFhYSG6du0KY2NjjBkzBoMGDYKnpyciIiLQvXt3VFZWIj09HZ6ennB0dBT0b4CIiIiIAEAqOgARERERUWMyMTFBbm4u3n77bXTr1g1Lly5FZGQkXF1dMWPGDHTv3h2Ojo7o0KEDDh48iPHjxyMwMBB+fn7o06cPDh06hGXLlqn8nu+++y5cXFwwcuRIdOjQATt27IBEIkF6ejqGDx8OX19fdOvWDRMnTkR5eTk6duwo6N0TERER0UMShUKhEB2CiIiIiIiIiIiIqDFxxycRERERERERERFpHRY+iYiIiIiIiIiISOuw8ElERERERERERERah4VPIiIiIiIiIiIi0josfBIREREREREREZHWYeGTiIiIiIiIiIiItA4Ln0RERERERERERKR1WPgkIiIiIiIiIiIircPCJxEREREREREREWkdFj6JiIiIiIiIiIhI67DwSURERERERERERFqHhU8iIiIiIiIiIiLSOv8HyRmEJv5mwIgAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 1600x500 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(16,5))\n",
    "sns.barplot(x=\"state\",y=\"number\",data=data3)\n",
    "plt.xticks(rotation=90)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "46ef3793-166a-4d94-a6bb-2656ccdc240e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "30650.129"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[data['state']=='Amazonas']['number'].sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "958574be-3b57-425e-b490-580a67835bd1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>year</th>\n",
       "      <th>number</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1998</td>\n",
       "      <td>946.000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1999</td>\n",
       "      <td>1061.000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2000</td>\n",
       "      <td>853.000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2001</td>\n",
       "      <td>1297.000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2002</td>\n",
       "      <td>2852.000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>2003</td>\n",
       "      <td>1524.268</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>2004</td>\n",
       "      <td>2298.207</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>2005</td>\n",
       "      <td>1657.128</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>2006</td>\n",
       "      <td>997.640</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>2007</td>\n",
       "      <td>589.601</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>2008</td>\n",
       "      <td>2717.000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>2009</td>\n",
       "      <td>1320.601</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>2010</td>\n",
       "      <td>2324.508</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>2011</td>\n",
       "      <td>1652.538</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>2012</td>\n",
       "      <td>1110.641</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>2013</td>\n",
       "      <td>905.217</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>2014</td>\n",
       "      <td>2385.909</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>2015</td>\n",
       "      <td>1189.994</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>2016</td>\n",
       "      <td>2060.972</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>2017</td>\n",
       "      <td>906.905</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    year    number\n",
       "0   1998   946.000\n",
       "1   1999  1061.000\n",
       "2   2000   853.000\n",
       "3   2001  1297.000\n",
       "4   2002  2852.000\n",
       "5   2003  1524.268\n",
       "6   2004  2298.207\n",
       "7   2005  1657.128\n",
       "8   2006   997.640\n",
       "9   2007   589.601\n",
       "10  2008  2717.000\n",
       "11  2009  1320.601\n",
       "12  2010  2324.508\n",
       "13  2011  1652.538\n",
       "14  2012  1110.641\n",
       "15  2013   905.217\n",
       "16  2014  2385.909\n",
       "17  2015  1189.994\n",
       "18  2016  2060.972\n",
       "19  2017   906.905"
      ]
     },
     "execution_count": 65,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data4=data[data['state']=='Amazonas']\n",
    "data5=data4.groupby('year')['number'].sum().reset_index()\n",
    "data5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "03503fda-f68b-441e-8eb4-460ae14307f5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: xlabel='year', ylabel='number'>"
      ]
     },
     "execution_count": 68,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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geUdd9wRU6ZMiXPOOSe7bdiwYXHUUUfFqFGjBJYAAAAAQJ3U6SvhW7dujeOOO26X7b169YotW7Z85qYAAAAAgKapToHld77znbjjjjt22X7XXXfFueeeW+vjPPvss3HaaadFWVlZZDKZ+O1vf1tj//nnnx+ZTKbGo0+fPjVqqqurY9SoUdGpU6do165dDBs2LFauXFmjZu3atVFeXh6FhYVRWFgY5eXl8dFHH9W6TwAAAAAgN2r9lfAxY8Zk/5zJZOKXv/xlPPnkk9kAccGCBbFixYr47ne/W+s337hxYxx99NHxve99L84666zd1gwePDimTp2afd6qVasa+0ePHh2PPvpozJw5Mzp27BiXX355DB06NBYuXBjNmzePiIgRI0bEypUro6KiIiIiLrrooigvL49HH3201r0CNCWTpw3Kdwv14vvls/LdAgAAAPup1oHlokWLajzv1atXRES88cYbERFx0EEHxUEHHRRLly6t9ZsPGTIkhgwZsteagoKCKC0t3e2+qqqquPvuu2PatGkxYMCAiIiYPn16dOnSJZ566qkYNGhQvPrqq1FRURELFiyI3r17R0TElClTom/fvrFs2bI44ogjat0vAAAAANCwah1Yzp07tyH72KOnn346iouL44ADDogTTzwxbrrppiguLo6IiIULF8ann34aAwcOzNaXlZVFjx49Yt68eTFo0KCYP39+FBYWZsPKiIg+ffpEYWFhzJs3b4+BZXV1dVRXV2efr1u3roEmBAAAAAC2q9M1LHNlyJAhMWPGjJgzZ07cdttt8eKLL8bJJ5+cDRIrKyujVatWceCBB9Z4XUlJSVRWVmZrtgecOyouLs7W7M64ceOy17wsLCyMLl261ONkAAAAAMDu1PoMyx198sknMXHixJg7d26sXr06tm3bVmP/H//4x3pp7tvf/nb2zz169IjjjjsuunbtGo8//ngMHz58j69LkiQymUz2+Y5/3lPNzq6++uoa1+1ct26d0BIAAAAAGlidAst//ud/jtmzZ8c3v/nN+Pu///u9Bn/1qXPnztG1a9d47bXXIiKitLQ0Nm/eHGvXrq1xluXq1aujX79+2Zr33ntvl2O9//77UVJSssf3KigoiIKCgnqeAAAAAADYmzoFlo8//ng88cQT8fWvf72++9mrNWvWxIoVK6Jz584R8dcb/7Rs2TJmz54dZ599dkRErFq1KpYsWRK33nprRET07ds3qqqq4oUXXoi///u/j4iI559/PqqqqrKhJgAAAACQDnUKLA8++OBo3779Z37zDRs2xOuvv559/uabb8bixYujqKgoioqKYuzYsXHWWWdF586d46233oqf/OQn0alTpzjzzDMjIqKwsDBGjhwZl19+eXTs2DGKioriiiuuiJ49e2bvGn7kkUfG4MGD48ILL4zJkydHRMRFF10UQ4cOdYdwAAAAAEiZOt1057bbbourrroqli9f/pne/A9/+EMce+yxceyxx0ZExJgxY+LYY4+Nf/u3f4vmzZvHyy+/HKeffnocfvjhcd5558Xhhx8e8+fPrxGWTpgwIc4444w4++yz4+tf/3q0bds2Hn300WjevHm2ZsaMGdGzZ88YOHBgDBw4MI466qiYNm3aZ+odAAAAAKh/dTrD8rjjjotPPvkkDjvssGjbtm20bNmyxv4PP/ywVsfp379/JEmyx/2zZs3a5zFat24dEydOjIkTJ+6xpqioKKZPn16rngAAAACA/KlTYHnOOefEO++8EzfffHOUlJTk7KY7AAAAAEDjVqfAct68eTF//vw4+uij67sfAAAAAKAJq9M1LL/yla/Epk2b6rsXAAAAAKCJq1Ngecstt8Tll18eTz/9dKxZsybWrVtX4wEAAAAAUBd1+kr44MGDIyLilFNOqbE9SZLIZDKxdevWz94ZAAAAANDk1CmwnDt3bn33AQAAAABQt8DyxBNPrO8+AAAAAADqFlg+++yze91/wgkn1KkZAAAAAKBpq1Ng2b9//122ZTKZ7J9dwxIAAAAAqIs63SV87dq1NR6rV6+OioqKOP744+PJJ5+s7x4BAAAAgCaiTmdYFhYW7rLt1FNPjYKCgvjRj34UCxcu/MyNAQAAAABNT53OsNyTgw46KJYtW1afhwQAAAAAmpA6nWH50ksv1XieJEmsWrUqbrnlljj66KPrpTEAAAAAoOmpU2B5zDHHRCaTiSRJamzv06dP/Md//Ee9NAYAAAAAND11CizffPPNGs+bNWsWBx10ULRu3bpemgIAAAAAmqY6BZZdu3aN3/3ud/G73/0uVq9eHdu2baux31mWAAAAAEBd1CmwvP766+OGG26I4447Ljp37hyZTKa++wIAAD6jYf/1aL5bqBePfPO0fLcAAORQnQLLO++8M+65554oLy+v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RlVVVXzta1/L1iRJEpdcckkUFxfHf//3f8cLL7wQp59+egwdOjTvC8Hdqa+5/+7v/i7uvffeuO2226Jt27ZRWloahx12WJSUlGRr8uWyyy6Ll156Kf7zP/9zl32ZTKbG8yRJdtm2s51rdldfm+M0tIaeO61yNfe7774bgwcPjm9961txwQUXfLam60Eu5v7xj38cixYtiieffDKaN28e3/3udyNJks/e/GfQkHNPnDgx1q1bF1dffXX9NVxPGvrz/tGPfhQnnnhiHHXUUXHBBRfEnXfeGXfffXesWbOmfgaoo4ace/s1ma+55po466yzolevXjF16tTIZDLx61//up4mqJtc/Xdt5cqVMWvWrBg5cuRna7ieNOTcaV6vNeTcTWm9tq9j1PU49a2h506rXM3d2Ndru9MU1ms7akrrtZ01lfXajprSem1Pcr1eE1imRK9evWLx4sXx0UcfxapVq6KioiLWrFkT3bp1y9YMHDgw3njjjVi9enV88MEHMW3atHjnnXeyNXPmzInHHnssZs6cGV//+tfja1/7Wvz7v/97tGnTJu699958jbZX9TF3xF8vZl5ZWRnvvPNOrFmzJsaOHRvvv/9+jZpcGzVqVDzyyCMxd+7cOOSQQ7LbS0tLIyJ2+VeN1atXZ//1o7S0NHv2wd5qdr5bekTE+++/v8u/ouRSQ8+dVrma+913342TTjop+vbtG3fddVdDjLJfcjV3p06d4vDDD49TTz01Zs6cGU888UQsWLCgIUaqlYaee86cObFgwYIoKCiIFi1axJe//OWIiDjuuOPivPPOa7C59iUfv999+vSJiIjXX3+9Xmaoi4aeu3PnzhER8dWvfjW7v6CgIA477LB4++2363+gWsrl5z116tTo2LFjDBs2rL7H2G+5+P1O43otF593Y1uv1UZjXK99nuVq7sa0XtsfjWm9VhuNcb1WV5/39VptNMb12v7K+XqtPi+ISe3ETjef2Z0///nPSbNmzZJZs2btseZ3v/tdkslkshfsfuSRR5JmzZol69evr1F3+OGHJzfddNNn7vuzaqi5d+fuu+9O2rZtW6sLQte3bdu2JZdeemlSVlaW/PnPf97t/tLS0uRnP/tZdlt1dfVuL17/wAMPZGvefffd3d505/nnn8/WLFiwIG8Xcc/V3DtKw0Xcczn3ypUrk+7duyf/9E//lGzZsqUBp9q3fHze27399ttJRCRz586tv4FqKVdzL1++PHn55Zezj1mzZiURkfzXf/1XsmLFigaeclf5/LwfffTRJCKS5cuX1+NEtZOruauqqpKCgoIaF3HffkHzyZMnN9R4e5Trz3vbtm1Jt27dkssvv7yBJqqdXM2dtvVaPn+/P+/rtR3t66Y7jWm9tqPPy013cjl3Y1uv7Wh/brrzeV+v7WhPczfG9dqO9ufz/ryv13a0p7kb43ptR/v6vPOxXhNY5sj69euTRYsWZe+GOH78+GTRokXZX+hf/epXydy5c5M33ngj+e1vf5t07do1GT58eI1j/Md//Ecyf/785PXXX0+mTZuWFBUVJWPGjMnuf//995OOHTsmw4cPTxYvXpwsW7YsueKKK5KWLVsmixcvzum82+Vi7iRJkokTJyYLFy5Mli1blkyaNClp06ZN8vOf/zxnc+7oBz/4QVJYWJg8/fTTyapVq7KPjz/+OFtzyy23JIWFhcmDDz6YvPzyy8k555yTdO7cOVm3bl225uKLL04OOeSQ5Kmnnkr++Mc/JieffHJy9NFH11j4DB48ODnqqKOS+fPnJ/Pnz0969uyZDB06NKfzbpfLuZcvX54sWrQouf7665MvfOEL2Z+xnf/PXy7kau533nkn+fKXv5ycfPLJycqVK2u8Vz7kau7nn38+mThxYrJo0aLkrbfeSubMmZN84xvfSL70pS8ln3zySaOde2dvvvlmXu86mau5582bl/174i9/+UvywAMPJGVlZcmwYcNyPnOS5Pbz/pd/+Zfk4IMPTmbNmpX86U9/SkaOHJkUFxcnH374YU5nTpLc/5w/9dRTSUQkr7zySs5m3J1czZ229VouP+/GuF5btWpVsmjRomTKlCnZu78vWrQoWbNmTbamMa7XajN3Y1yv7Wvuxrpe29fcjXW9Vpuf8x01lvXavuZurOu12nzejXG9Vtuf83ys1wSWObI9rd75cd555yVJkiQ///nPk0MOOSRp2bJlcuihhybXXnttUl1dXeMYV111VVJSUpK0bNky6d69e3Lbbbcl27Ztq1Hz4osvJgMHDkyKioqS9u3bJ3369EmeeOKJXI25i1zNXV5enhQVFSWtWrVKjjrqqOS+++7L1Yi72N28EZFMnTo1W7Nt27bkuuuuS0pLS5OCgoLkhBNOSF5++eUax9m0aVNy2WWXJUVFRUmbNm2SoUOHJm+//XaNmjVr1iTnnntu0r59+6R9+/bJueeem5ezFJIkt3Ofd955u32vfPwLbq7mnjp16h7fKx9yNfdLL72UnHTSSUlRUVFSUFCQfPGLX0wuvvjiZOXKlbkatYZc/pzvKN8L4FzNvXDhwqR3795JYWFh0rp16+SII45IrrvuumTjxo25GrWGXH7emzdvTi6//PKkuLg4ad++fTJgwIBkyZIluRhzF7n+OT/nnHOSfv36NfRY+5TLudO0Xsvl3I1xvXbdddft8ziNcb1Wm7kb43ptX3M31vXavuZurOu12vyc76ixrNf2NXdjXa/V5vNujOu12v6c52O9lkmSPF8FFwAAAADgb9x0BwAAAABIDYElAAAAAJAaAksAAAAAIDUElgAAAABAaggsAQAAAIDUEFgCAAAAAKkhsAQAAAAAUkNgCQAAAACkhsASAAAAAEgNgSUAAE3e1q1bY9u2bfluAwCAEFgCAJAy9913X3Ts2DGqq6trbD/rrLPiu9/9bkREPProo9GrV69o3bp1HHbYYXH99dfHli1bsrXjx4+Pnj17Rrt27aJLly5xySWXxIYNG7L777nnnjjggAPisccei69+9atRUFAQy5cvz82AAADslcASAIBU+da3vhVbt26NRx55JLvtgw8+iMceeyy+973vxaxZs+I73/lO/PCHP4xXXnklJk+eHPfcc0/cdNNN2fpmzZrFL37xi1iyZEnce++9MWfOnLjyyitrvM/HH38c48aNi1/+8pexdOnSKC4uztmMAADsWSZJkiTfTQAAwI4uueSSeOutt+KJJ56IiIif//zn8Ytf/CJef/31OPHEE2PIkCFx9dVXZ+unT58eV155Zbz77ru7Pd6vf/3r+MEPfhAffPBBRPz1DMvvfe97sXjx4jj66KMbfiAAAGpNYAkAQOosWrQojj/++Fi+fHkcfPDBccwxx8RZZ50VP/3pT6Ndu3axbdu2aN68ebZ+69at8cknn8TGjRujbdu2MXfu3Lj55pvjlVdeiXXr1sWWLVvik08+iQ0bNkS7du3innvuie9///vxySefRCaTyeOkAADsrEW+GwAAgJ0de+yxcfTRR8d9990XgwYNipdffjkeffTRiIjYtm1bXH/99TF8+PBdXte6detYvnx5/MM//ENcfPHF8b//9/+OoqKieO6552LkyJHx6aefZmvbtGkjrAQASCGBJQAAqXTBBRfEhAkT4p133okBAwZEly5dIiLia1/7Wixbtiy+/OUv7/Z1f/jDH2LLli1x2223RbNmf71k+69+9auc9Q0AwGcjsAQAIJXOPffcuOKKK2LKlClx3333Zbf/27/9WwwdOjS6dOkS3/rWt6JZs2bx0ksvxcsvvxw33nhjfOlLX4otW7bExIkT47TTTovf//73ceedd+ZxEgAA9oe7hAMAkEodOnSIs846K77whS/EGWeckd0+aNCgeOyxx2L27Nlx/PHHR58+fWL8+PHRtWvXiIg45phjYvz48fGzn/0sevToETNmzIhx48blaQoAAPaXm+4AAJBap556ahx55JHxi1/8It+tAACQIwJLAABS58MPP4wnn3wyzj333HjllVfiiCOOyHdLAADkiGtYAgCQOl/72tdi7dq18bOf/UxYCQDQxDjDEgAAAABIDTfdAQAAAABSQ2AJAAAAAKSGwBIAAAAASA2BJQAAAACQGgJLAAAAACA1BJYAAAAAQGoILAEAAACA1BBYAgAAAACpIbAEAAAAAFLj/wMKbiOMb1MKAgAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 1600x500 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(16,5))\n",
    "sns.barplot(x=\"year\",y=\"number\",data=data5)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "114cbd09-70c8-4eab-81f0-887635eb1506",
   "metadata": {},
   "outputs": [],
   "source": [
    "data6=data[data['state']=='Amazonas']\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "8a654def-e3ba-4d4d-b500-8cc1a94098ad",
   "metadata": {},
   "outputs": [],
   "source": [
    "day=data6.groupby(data6['date'].dt.dayofweek).number.sum()\n",
    "import calendar\n",
    "\n",
    "day.index=[calendar.day_name[x] for x in range(0,7)]\n",
    "day=day.reset_index()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "523ff02f-ef70-4fa1-8b44-85438d1005a5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>index</th>\n",
       "      <th>number</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Monday</td>\n",
       "      <td>1886.601</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Tuesday</td>\n",
       "      <td>6474.217</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Wednesday</td>\n",
       "      <td>3910.177</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Thursday</td>\n",
       "      <td>5754.802</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Friday</td>\n",
       "      <td>5446.480</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Saturday</td>\n",
       "      <td>4162.666</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Sunday</td>\n",
       "      <td>3015.186</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       index    number\n",
       "0     Monday  1886.601\n",
       "1    Tuesday  6474.217\n",
       "2  Wednesday  3910.177\n",
       "3   Thursday  5754.802\n",
       "4     Friday  5446.480\n",
       "5   Saturday  4162.666\n",
       "6     Sunday  3015.186"
      ]
     },
     "execution_count": 87,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "day"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "cc7110f3-8d90-49e6-adce-80e4abff140f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: xlabel='index', ylabel='number'>"
      ]
     },
     "execution_count": 89,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABSwAAAHACAYAAACoIiYOAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjguMCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy81sbWrAAAACXBIWXMAAA9hAAAPYQGoP6dpAABK+klEQVR4nO3dfbwWdZ0//teRexCOgsCRBG+RMPGWjZtKIEXUEKstW0m8N41S8bZczchVNH6rsslmat6DsW6lW2YnbwJSAUUSb5C1GzU1QbzBAygCwvz+8Mu1Hg8qIniGeD4fj+shM/Oeud5zPeaM13mdz8xUFUVRBAAAAACgBDZr7AYAAAAAAFYTWAIAAAAApSGwBAAAAABKQ2AJAAAAAJSGwBIAAAAAKA2BJQAAAABQGgJLAAAAAKA0BJYAAAAAQGk0bewGNharVq3KCy+8kLZt26aqqqqx2wEAAACAjUpRFFm8eHG6dOmSzTZ773GUAsu19MILL6Rr166N3QYAAAAAbNSee+65bLPNNu+5XGC5ltq2bZvk7Q+0Xbt2jdwNAAAAAGxcFi1alK5du1ZytvcisFxLqy8Db9euncASAAAAANbRB91u0UN3AAAAAIDSEFgCAAAAAKUhsAQAAAAASkNgCQAAAACUhsASAAAAACgNgSUAAAAAUBoCSwAAAACgNASWAAAAAEBpCCwBAAAAgNIQWAIAAAAApSGwBAAAAABKQ2AJAAAAAJSGwBIAAAAAKA2BJQAAAABQGgJLAAAAAKA0mjZ2A8DG59nzezV2C2xkup33WGO3AAAAwEbCCEsAAAAAoDQElgAAAABAaQgsAQAAAIDSEFgCAAAAAKUhsAQAAAAASkNgCQAAAACUhsASAAAAACgNgSUAAAAAUBoCSwAAAACgNASWAAAAAEBpCCwBAAAAgNIQWAIAAAAApSGwBAAAAABKQ2AJAAAAAJSGwBIAAAAAKA2BJQAAAABQGgJLAAAAAKA0BJYAAAAAQGkILAEAAACA0hBYAgAAAAClIbAEAAAAAEpDYAkAAAAAlEajB5Z///vfc/jhh6dDhw5p3bp19thjj8yaNauyvCiKjB49Ol26dEmrVq0ycODAzJkzp942li1blpNOOilbbbVV2rRpk2HDhuX555+vV7Nw4cKMGDEi1dXVqa6uzogRI/Laa699HLsIAAAAAKylRg0sFy5cmM985jNp1qxZfvvb3+aJJ57IJZdcki222KJSM3bs2Fx66aUZP358Zs6cmZqamgwePDiLFy+u1IwaNSq33nprJk2alPvuuy9LlizJ0KFDs3LlykrN8OHDM3v27NTW1qa2tjazZ8/OiBEjPs7dBQAAAAA+QFVRFEVjvfl3v/vd3H///bn33nvXuLwoinTp0iWjRo3Kd77znSRvj6bs3LlzfvjDH+aEE05IXV1dOnbsmJtuuilf+9rXkiQvvPBCunbtmjvuuCNDhgzJ3Llzs8suu2TGjBnp06dPkmTGjBnp169f/vd//zc9evT4wF4XLVqU6urq1NXVpV27duvpE4CN07Pn92rsFtjIdDvvscZuAQAAgEa2tvlao46w/NWvfpXevXvnq1/9ajp16pQ999wzV199dWX5008/nfnz52f//fevzGvRokUGDBiQadOmJUlmzZqVFStW1Kvp0qVLdt1110rN9OnTU11dXQkrk6Rv376prq6u1LzbsmXLsmjRonovAAAAAGDDatTA8qmnnsoVV1yR7t2753e/+11OPPHEnHzyybnxxhuTJPPnz0+SdO7cud56nTt3riybP39+mjdvni233PJ9azp16tTg/Tt16lSpebeLLrqocr/L6urqdO3a9aPtLAAAAADwgRo1sFy1alX22muvjBkzJnvuuWdOOOGEHH/88bniiivq1VVVVdWbLoqiwbx3e3fNmurfbztnn3126urqKq/nnntubXcLAAAAAFhHjRpYbr311tlll13qzevZs2eeffbZJElNTU2SNBgFuWDBgsqoy5qamixfvjwLFy5835oXX3yxwfu/9NJLDUZvrtaiRYu0a9eu3gsAAAAA2LAaNbD8zGc+kyeffLLevD/96U/ZdtttkyTbb799ampqctddd1WWL1++PFOnTk3//v2TJHvvvXeaNWtWr2bevHl5/PHHKzX9+vVLXV1dHnzwwUrNAw88kLq6ukoNAAAAAND4mjbmm5966qnp379/xowZk0MPPTQPPvhgrrrqqlx11VVJ3r6Me9SoURkzZky6d++e7t27Z8yYMWndunWGDx+eJKmurs6xxx6b008/PR06dEj79u1zxhlnpFevXtlvv/2SvD1q84ADDsjxxx+fK6+8MknyjW98I0OHDl2rJ4QDAAAAAB+PRg0s/+mf/im33nprzj777Jx//vnZfvvtM27cuHz9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981jjz2W2bNnV169e/fO17/+9cyePTs77LBDampqctddd1XWWb58eaZOnZr+/fsnSfbee+80a9asXs28efPy+OOPV2r69euXurq6PPjgg5WaBx54IHV1dZUaAAAAAKAcGu0elm3bts2uu+5ab16bNm3SoUOHyvxRo0ZlzJgx6d69e7p3754xY8akdevWGT58eJKkuro6xx57bE4//fR06NAh7du3zxlnnJFevXpVHuLTs2fPHHDAATn++ONz5ZVXJkm+8Y1vZOjQoenRo8fHuMcAAAAAwAdp1IfufJCzzjorS5cuzciRI7Nw4cL06dMnd955Z9q2bVupueyyy9K0adMceuihWbp0afbdd99cf/31adKkSaVm4sSJOfnkkytPEx82bFjGjx//se8PAOXwmcs/09gtsJG5/6T7G7sFAADYZJQqsJwyZUq96aqqqowePTqjR49+z3VatmyZyy+/PJdffvl71rRv3z4TJkxYT10CAAAAABtKo93DEgAAAADg3QSWAAAAAEBpCCwBAAAAgNL40IFlURT529/+lqVLl26IfgAAAACATdg6BZbdu3fP888/vyH6AQAAAAA2YR86sNxss83SvXv3vPLKKxuiHwAAAABgE7ZO97AcO3ZszjzzzDz++OPrux8AAAAAYBPWdF1WOvzww/PGG29k9913T/PmzdOqVat6y1999dX10hwAAAAAsGlZp8By3Lhx67kNAAAAAIB1DCyPPPLI9d0HAAAAAMC63cMySf7617/m3HPPzWGHHZYFCxYkSWprazNnzpz11hwAAAAAsGlZp8By6tSp6dWrVx544IH88pe/zJIlS5Ikjz76aL7//e+v1wYBAAAAgE3HOgWW3/3ud3PBBRfkrrvuSvPmzSvzBw0alOnTp6+35gAAAACATcs6BZaPPfZYvvSlLzWY37Fjx7zyyisfuSkAAAAAYNO0ToHlFltskXnz5jWY//DDD+cTn/jER24KAAAAANg0rVNgOXz48HznO9/J/PnzU1VVlVWrVuX+++/PGWeckSOOOGJ99wgAAAAAbCLWKbC88MIL061bt3ziE5/IkiVLsssuu2SfffZJ//79c+65567vHgEAAACATUTTdVmpWbNmmThxYs4///w8/PDDWbVqVfbcc8907959ffcHAAAAAGxC1imwXG3HHXfMDjvskCSpqqpaLw0BAAAAAJuudbokPEmuueaa7LrrrmnZsmVatmyZXXfdNT/96U/XZ28AAAAAwCZmnUZYfu9738tll12Wk046Kf369UuSTJ8+PaeeemqeeeaZXHDBBeu1SQAAAABg07BOgeUVV1yRq6++Oocddlhl3rBhw7LbbrvlpJNOElgCAAAAAOtknS4JX7lyZXr37t1g/t5775233nrrIzcFAAAAAGya1imwPPzww3PFFVc0mH/VVVfl61//+kduCgAAAADYNK31JeGnnXZa5d9VVVX56U9/mjvvvDN9+/ZNksyYMSPPPfdcjjjiiPXfJQAAAACwSVjrwPLhhx+uN7333nsnSf76178mSTp27JiOHTtmzpw567E9AAAAAGBTstaB5eTJkzdkHwAAAAAA63YPSwAAAACADWGtR1i+05tvvpnLL788kydPzoIFC7Jq1ap6y//4xz+ul+YAAAAAgE3LOgWWxxxzTO6666585Stfyac//elUVVWt774AAAAAgE3QOgWWv/nNb3LHHXfkM5/5zPruBwAAAADYhK3TPSw/8YlPpG3btuu7FwAAAABgE7dOgeUll1yS73znO/nb3/62vvsBAAAAADZh63RJeO/evfPmm29mhx12SOvWrdOsWbN6y1999dX10hwAAAAAsGlZp8DysMMOy9///veMGTMmnTt39tAdAAAAAGC9WKfActq0aZk+fXp233339d0PAAAAALAJW6d7WH7yk5/M0qVL13cvAAAAAMAmbp0Cy4svvjinn356pkyZkldeeSWLFi2q9wIAAAAAWBfrdEn4AQcckCTZd999680viiJVVVVZuXLlR+8MAAAAANjkrFNgOXny5PXdBwAAAADAugWWAwYMWN99AAAAAACsW2D5hz/84X2X77PPPuvUDAAAAACwaVunwHLgwIEN5lVVVVX+7R6WAAAAAMC6WKenhC9cuLDea8GCBamtrc0//dM/5c4771zfPQIAAAAAm4h1GmFZXV3dYN7gwYPTokWLnHrqqZk1a9ZHbgwAAAAA2PSs0wjL99KxY8c8+eST63OTAAAAAMAmZJ0Cy0cffbTe65FHHkltbW2++c1vZvfdd1/r7VxxxRXZbbfd0q5du7Rr1y79+vXLb3/728ryoigyevTodOnSJa1atcrAgQMzZ86cettYtmxZTjrppGy11VZp06ZNhg0blueff75ezcKFCzNixIhUV1enuro6I0aMyGuvvbYuuw4AAAAAbEDrFFjuscce2XPPPbPHHntU/n3QQQdl+fLlueaaa9Z6O9tss00uvvjiPPTQQ3nooYfy+c9/PoccckgllBw7dmwuvfTSjB8/PjNnzkxNTU0GDx6cxYsXV7YxatSo3HrrrZk0aVLuu+++LFmyJEOHDq334J/hw4dn9uzZqa2tTW1tbWbPnp0RI0asy64DAAAAABvQOt3D8umnn643vdlmm6Vjx45p2bLlh9rOwQcfXG/6wgsvzBVXXJEZM2Zkl112ybhx43LOOefky1/+cpLkhhtuSOfOnXPzzTfnhBNOSF1dXa655prcdNNN2W+//ZIkEyZMSNeuXXP33XdnyJAhmTt3bmprazNjxoz06dMnSXL11VenX79+efLJJ9OjR491+QgAAAAAgA1gnQLLbbfdNvfcc0/uueeeLFiwIKtWraq3/Nprr/3Q21y5cmX++7//O6+//nr69euXp59+OvPnz8/+++9fqWnRokUGDBiQadOm5YQTTsisWbOyYsWKejVdunTJrrvummnTpmXIkCGZPn16qqurK2FlkvTt2zfV1dWZNm3aewaWy5Yty7JlyyrTixYt+tD7BAAAAFA2cy/8fWO3wEao5zmf/9jea50uCf/BD36Q/fffP/fcc09efvnlLFy4sN7rw3jsscey+eabp0WLFjnxxBNz6623Zpdddsn8+fOTJJ07d65X37lz58qy+fPnp3nz5tlyyy3ft6ZTp04N3rdTp06VmjW56KKLKve8rK6uTteuXT/UfgEAAAAAH946jbD8yU9+kuuvv3693AeyR48emT17dl577bX84he/yJFHHpmpU6dWlldVVdWrL4qiwbx3e3fNmuo/aDtnn312TjvttMr0okWLhJYAAAAAsIGt0wjL5cuXp3///uulgebNm2ennXZK7969c9FFF2X33XfPf/zHf6SmpiZJGoyCXLBgQWXUZU1NTZYvX95gVOe7a1588cUG7/vSSy81GL35Ti1atKg8vXz1CwAAAADYsNYpsDzuuONy8803r+9ekrw98nHZsmXZfvvtU1NTk7vuuquybPny5Zk6dWolLN17773TrFmzejXz5s3L448/Xqnp169f6urq8uCDD1ZqHnjggdTV1a230BUAAAAAWD/W6ZLwN998M1dddVXuvvvu7LbbbmnWrFm95Zdeeulabedf//Vfc+CBB6Zr165ZvHhxJk2alClTpqS2tjZVVVUZNWpUxowZk+7du6d79+4ZM2ZMWrduneHDhydJqqurc+yxx+b0009Phw4d0r59+5xxxhnp1atX5anhPXv2zAEHHJDjjz8+V155ZZLkG9/4RoYOHeoJ4QAAAABQMusUWD766KPZY489kiSPP/54vWUfdH/Jd3rxxRczYsSIzJs3L9XV1dltt91SW1ubwYMHJ0nOOuusLF26NCNHjszChQvTp0+f3HnnnWnbtm1lG5dddlmaNm2aQw89NEuXLs2+++6b66+/Pk2aNKnUTJw4MSeffHLlaeLDhg3L+PHj12XXAQAAAIANaJ0Cy8mTJ6+XN7/mmmved3lVVVVGjx6d0aNHv2dNy5Ytc/nll+fyyy9/z5r27dtnwoQJ69omAAAAAPAxWad7WAIAAAAAbAgCSwAAAACgNASWAAAAAEBpCCwBAAAAgNIQWAIAAAAApSGwBAAAAABKQ2AJAAAAAJSGwBIAAAAAKA2BJQAAAABQGgJLAAAAAKA0BJYAAAAAQGkILAEAAACA0hBYAgAAAAClIbAEAAAAAEpDYAkAAAAAlIbAEgAAAAAoDYElAAAAAFAaAksAAAAAoDQElgAAAABAaQgsAQAAAIDSEFgCAAAAAKUhsAQAAAAASkNgCQAAAACUhsASAAAAACgNgSUAAAAAUBoCSwAAAACgNASWAAAAAEBpCCwBAAAAgNIQWAIAAAAApSGwBAAAAABKQ2AJAAAAAJSGwBIAAAAAKA2BJQAAAABQGgJLAAAAAKA0BJYAAAAAQGkILAEAAACA0hBYAgAAAAClIbAEAAAAAEpDYAkAAAAAlIbAEgAAAAAoDYElAAAAAFAaAksAAAAAoDQElgAAAABAaQgsAQAAAIDSEFgCAAAAAKXRqIHlRRddlH/6p39K27Zt06lTp3zxi1/Mk08+Wa+mKIqMHj06Xbp0SatWrTJw4MDMmTOnXs2yZcty0kknZauttkqbNm0ybNiwPP/88/VqFi5cmBEjRqS6ujrV1dUZMWJEXnvttQ29iwAAAADAh9CogeXUqVPzrW99KzNmzMhdd92Vt956K/vvv39ef/31Ss3YsWNz6aWXZvz48Zk5c2ZqamoyePDgLF68uFIzatSo3HrrrZk0aVLuu+++LFmyJEOHDs3KlSsrNcOHD8/s2bNTW1ub2trazJ49OyNGjPhY9xcAAAAAeH9NG/PNa2tr601fd9116dSpU2bNmpV99tknRVFk3LhxOeecc/LlL385SXLDDTekc+fOufnmm3PCCSekrq4u11xzTW666abst99+SZIJEyaka9euufvuuzNkyJDMnTs3tbW1mTFjRvr06ZMkufrqq9OvX788+eST6dGjx8e74wAAAADAGpXqHpZ1dXVJkvbt2ydJnn766cyfPz/7779/paZFixYZMGBApk2bliSZNWtWVqxYUa+mS5cu2XXXXSs106dPT3V1dSWsTJK+ffumurq6UvNuy5Yty6JFi+q9AAAAAIANqzSBZVEUOe200/LZz342u+66a5Jk/vz5SZLOnTvXq+3cuXNl2fz589O8efNsueWW71vTqVOnBu/ZqVOnSs27XXTRRZX7XVZXV6dr164fbQcBAAAAgA9UmsDy29/+dh599NH87Gc/a7Csqqqq3nRRFA3mvdu7a9ZU/37bOfvss1NXV1d5Pffcc2uzGwAAAADAR1CKwPKkk07Kr371q0yePDnbbLNNZX5NTU2SNBgFuWDBgsqoy5qamixfvjwLFy5835oXX3yxwfu+9NJLDUZvrtaiRYu0a9eu3gsAAAAA2LAaNbAsiiLf/va388tf/jK///3vs/3229dbvv3226empiZ33XVXZd7y5cszderU9O/fP0my9957p1mzZvVq5s2bl8cff7xS069fv9TV1eXBBx+s1DzwwAOpq6ur1AAAAAAAja9RnxL+rW99KzfffHP+53/+J23btq2MpKyurk6rVq1SVVWVUaNGZcyYMenevXu6d++eMWPGpHXr1hk+fHil9thjj83pp5+eDh06pH379jnjjDPSq1evylPDe/bsmQMOOCDHH398rrzyyiTJN77xjQwdOtQTwgEAAACgRBo1sLziiiuSJAMHDqw3/7rrrstRRx2VJDnrrLOydOnSjBw5MgsXLkyfPn1y5513pm3btpX6yy67LE2bNs2hhx6apUuXZt99983111+fJk2aVGomTpyYk08+ufI08WHDhmX8+PEbdgcBAAAAgA+lUQPLoig+sKaqqiqjR4/O6NGj37OmZcuWufzyy3P55Ze/Z0379u0zYcKEdWkTAAAAAPiYNGpguSna+8wbG7sFNkKz/r8jGrsFAAAAgI9FKZ4SDgAAAACQCCwBAAAAgBIRWAIAAAAApSGwBAAAAABKQ2AJAAAAAJSGwBIAAAAAKA2BJQAAAABQGgJLAAAAAKA0BJYAAAAAQGkILAEAAACA0hBYAgAAAAClIbAEAAAAAEpDYAkAAAAAlIbAEgAAAAAoDYElAAAAAFAaAksAAAAAoDQElgAAAABAaQgsAQAAAIDSEFgCAAAAAKUhsAQAAAAASkNgCQAAAACUhsASAAAAACgNgSUAAAAAUBoCSwAAAACgNASWAAAAAEBpCCwBAAAAgNIQWAIAAAAApSGwBAAAAABKQ2AJAAAAAJSGwBIAAAAAKA2BJQAAAABQGgJLAAAAAKA0BJYAAAAAQGkILAEAAACA0hBYAgAAAAClIbAEAAAAAEpDYAkAAAAAlIbAEgAAAAAoDYElAAAAAFAaAksAAAAAoDQElgAAAABAaQgsAQAAAIDSEFgCAAAAAKUhsAQAAAAASkNgCQAAAACURqMGln/4wx9y8MEHp0uXLqmqqsptt91Wb3lRFBk9enS6dOmSVq1aZeDAgZkzZ069mmXLluWkk07KVlttlTZt2mTYsGF5/vnn69UsXLgwI0aMSHV1daqrqzNixIi89tprG3jvAAAAAIAPq1EDy9dffz277757xo8fv8blY8eOzaWXXprx48dn5syZqampyeDBg7N48eJKzahRo3Lrrbdm0qRJue+++7JkyZIMHTo0K1eurNQMHz48s2fPTm1tbWprazN79uyMGDFig+8fAAAAAPDhNG3MNz/wwANz4IEHrnFZURQZN25czjnnnHz5y19Oktxwww3p3Llzbr755pxwwgmpq6vLNddck5tuuin77bdfkmTChAnp2rVr7r777gwZMiRz585NbW1tZsyYkT59+iRJrr766vTr1y9PPvlkevTo8fHsLAAAAADwgUp7D8unn3468+fPz/7771+Z16JFiwwYMCDTpk1LksyaNSsrVqyoV9OlS5fsuuuulZrp06enurq6ElYmSd++fVNdXV2pWZNly5Zl0aJF9V4AAAAAwIZV2sBy/vz5SZLOnTvXm9+5c+fKsvnz56d58+bZcsst37emU6dODbbfqVOnSs2aXHTRRZV7XlZXV6dr164faX8AAAAAgA9W2sBytaqqqnrTRVE0mPdu765ZU/0Hbefss89OXV1d5fXcc899yM4BAAAAgA+rtIFlTU1NkjQYBblgwYLKqMuamposX748Cxcu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ms2bN6/y7//6r//KeeedlyeffLIyb/WxDB+nQYMGZcmSJXnooYfSt2/fJG8HkzU1NZk5c2beeOONtG7dOkkyZcqUdOnSJTvvvHNjtgxrbW3OuwsXLtwg7718+fI0b958g2wbPsgBBxyQ6667rt68jh071ptefYzW1NR8nK2xifvnf/7nrFixIjfccEN22GGHvPjii7nnnnvy6quvfuy9rFixIs2aNfvY35d/PGU6rtlwjLBkrey1117p1q1bfvnLX1bm/fKXv0zXrl2z5557VuYtW7YsJ598cjp16pSWLVvms5/9bGbOnFlZPmXKlFRVVeWee+5J796907p16/Tv37/eLzNJcvHFF6dz585p27Ztjj322Lz55pv1ls+cOTODBw/OVlttlerq6gwYMCB//OMfK8uPOeaYDB06tN46b731VmpqanLttdeul8+E8qupqam8qqurU1VVVZmura3NtttuW6/+tttuS1VVVb15v/71r7P33nunZcuW2WGHHfKDH/yg3si40aNHV/6y16VLl5x88smVZQsWLMjBBx+cVq1aZfvtt8/EiRMb9HjppZemV69eadOmTbp27ZqRI0dmyZIlSZLXX3897dq1y89//vMGPbVp0yaLFy/+yJ8RH78ePXqkS5cumTJlSmXelClTcsghh2THHXfMtGnT6s0fNGhQli9fnrPOOiuf+MQn0qZNm/Tp06fe+snbIyC6deuW1q1b50tf+lJeeeWVestXX8Jy0003Zbvttkt1dXX+5V/+pd5xVBRFxo4dmx122CGtWrXK7rvvXu/4W7hwYb7+9a+nY8eOadWqVbp3717vF/QHH3wwe+65Z1q2bJnevXvn4YcfrtfDypUrc+yxx2b77bdPq1at0qNHj/zHf/xHZfkf/vCHNGvWLPPnz6+33umnn5599tln7T9kGs37nXdXz1vtqaeeyqBBg9K6devsvvvu9UZFrOmSq3HjxmW77barTK++hPCiiy6qF+z/+Mc/Tvfu3dOyZct07tw5X/nKVyrrvP766zniiCOy+eabZ+utt84ll1zSYB8mTJiQ3r17p23btqmpqcnw4cOzYMGCJG//jOy0007593//93rrPP7449lss83y17/+dZ0/OzZuq0f4vPO177775tvf/nZOO+20bLXVVhk8eHCShpeEO3eyobz22mu577778sMf/jCDBg3Ktttum09/+tM5++yz84UvfCHJ+38XnTJlSo4++ujU1dVVRg6PHj06yZpvbbDFFlvk+uuvT/J/tza45ZZbMnDgwLRs2TITJkzIypUrc9ppp2WLLbZIhw4dctZZZ6Uoinrbqa2tzWc/+9lKzdChQ+udXz//+c/n29/+dr11XnnllbRo0SK///3v1+MnSBl90HG9pttqvPbaa6mqqqp8f5ZLbBwElqy1o48+ut4vptdee22OOeaYejVnnXVWfvGLX+SGG27IH//4x+y0004ZMmRIg790nHPOObnkkkvy0EMPpWnTpvW2c8stt+T73/9+Lrzwwjz00EPZeuut8+Mf/7je+osXL86RRx6Ze++9NzNmzEj37t1z0EEHVX7xPu6441JbW1tvpMcdd9yRJUuW5NBDD11vnwn/2H73u9/l8MMPz8knn5wnnngiV155Za6//vpceOGFSZKf//znueyyy3LllVfmz3/+c2677bb06tWrsv5RRx2VZ555Jr///e/z85//PD/+8Y8rv/Suttlmm+VHP/pRHn/88dxwww35/e9/n7POOitJ0qZNm/zLv/xLgxEb1113Xb7yla+kbdu2G/gTYEMZOHBgJk+eXJmePHlyBg4cmAEDBlTmL1++PNOnT8+gQYNy9NFH5/7778+kSZPy6KOP5qtf/WoOOOCA/PnPf06SPPDAAznmmGMycuTIzJ49O4MGDcoFF1zQ4H3/+te/5rbbbsvtt9+e22+/PVOnTs3FF19cWX7uuefmuuuuyxVXXJE5c+bk1FNPzeGHH56pU6cmSb73ve/liSeeyG9/+9vMnTs3V1xxRbbaaqskbwdBQ4cOTY8ePTJr1qyMHj06Z5xxRr33X7VqVbbZZpvccssteeKJJ3LeeeflX//1X3PLLbckSfbZZ5/ssMMOuemmmyrrvPXWW5kwYUKOPvro9fHRUyLnnHNOzjjjjMyePTs777xzDjvssHp/EFob99xzT+bOnZu77rort99+ex566KGcfPLJOf/88/Pkk0+mtra2XmBz5plnZvLkybn11ltz5513ZsqUKZk1a1a9bS5fvjz/9m//lkceeSS33XZbnn766cql7FVVVTnmmGManJevvfbafO5zn8uOO+64bh8G/7BuuOGGNG3aNPfff3+uvPLKBsudO9mQNt9882y++ea57bbbsmzZsjXWvN930f79+2fcuHFp165d5s2bl3nz5jU4Pj/Id77znZx88smZO3duhgwZkksuuSTXXnttrrnmmtx333159dVXc+utt9Zb5/XXX89pp52WmTNn5p577slmm22WL33pS1m1alWSt3/Xu/nmm+vt08SJE9OlS5cMGjToQ/XHxmdtjuu1JZcouQI+wJFHHlkccsghxUsvvVS0aNGiePrpp4tnnnmmaNmyZfHSSy8VhxxySHHkkUcWS5YsKZo1a1ZMnDixsu7y5cuLLl26FGPHji2KoigmT55cJCnuvvvuSs1vfvObIkmxdOnSoiiKol+/fsWJJ55Yr4c+ffoUu++++3v2+NZbbxVt27Ytfv3rX1fm7bLLLsUPf/jDyvQXv/jF4qijjvpInwUbr+uuu66orq5+z+miKIpbb721eOdp8XOf+1wxZsyYejU33XRTsfXWWxdFURSXXHJJsfPOOxfLly9v8H5PPvlkkaSYMWNGZd7cuXOLJMVll132nn3ecsstRYcOHSrTDzzwQNGkSZPi73//e1EURfHSSy8VzZo1K6ZMmfKB+0x5XXXVVUWbNm2KFStWFIsWLSqaNm1avPjii8WkSZOK/v37F0VRFFOnTi2SFH/5y1+KqqqqyjGw2r777lucffbZRVEUxWGHHVYccMAB9ZZ/7Wtfq3eMf//73y9at25dLFq0qDLvzDPPLPr06VMURVEsWbKkaNmyZTFt2rR62zn22GOLww47rCiKojj44IOLo48+eo37dOWVVxbt27cvXn/99cq8K664okhSPPzww+/5WYwcObL453/+58r0D3/4w6Jnz56V6dtuu63YfPPNiyVLlrznNiinNZ1ni6Ionn766SJJ8dOf/rQyb86cOUWSYu7cuUVRvH28vvv/+5dddlmx7bbbVqaPPPLIonPnzsWyZcsq837xi18U7dq1q3ecr7Z48eKiefPmxaRJkyrzXnnllaJVq1bFKaec8p778eCDDxZJisWLFxdFURQvvPBC0aRJk+KBBx4oiuLt7zodO3Ysrr/++vfcBv/YjjzyyKJJkyZFmzZtKq+vfOUrxYABA4o99tijQX2S4tZbby2KwrmTDe/nP/95seWWWxYtW7Ys+vfvX5x99tnFI4888p717/4u+l7n8ncex6tVV1cX1113XVEU/3euHzduXL2arbfeurj44osr0ytWrCi22Wab4pBDDnnPnhYsWFAkKR577LGiKIrizTffLNq3b1/813/9V6Vmjz32KEaPHv2e2+Afy/sd16uPvXeeQxcuXFgkKSZPnlwUhVxiY2GEJWttq622yhe+8IXccMMNue666/KFL3yhMrImeXvkzooVK/KZz3ymMq9Zs2b59Kc/nblz59bb1m677Vb599Zbb50klZFnc+fOTb9+/erVv3t6wYIFOfHEE7Pzzjunuro61dXVWbJkSZ599tlKzXHHHVcZAbFgwYL85je/aTAiFN7PrFmzcv7551f+irf55pvn+OOPz7x58/LGG2/kq1/9apYuXZoddtghxx9/fG699dbK6KC5c+emadOm6d27d2V7n/zkJxvctHzy5MkZPHhwPvGJT6Rt27Y54ogj8sorr+T1119Pknz605/Opz71qdx4441JkptuuindunVziddGbtCgQXn99dczc+bM3Hvvvdl5553TqVOnDBgwIDNnzszrr7+eKVOmpFu3bvnjH/+Yoiiy88471zsWp06dWrk8am3Om8nbT6l/58jcrbfeunLufeKJJ/Lmm29m8ODB9d7nxhtvrLzPN7/5zUyaNCl77LFHzjrrrHqXr8+dOze777575f6b79XDT37yk/Tu3TsdO3bM5ptvnquvvrreufuoo47KX/7yl8yYMSPJ2yPXDj300LRp0+ZDf86U2/t9F1hbvXr1qnffysGDB2fbbbfNDjvskBEjRmTixIl54403krz9PWX58uX1jsv27dunR48e9bb58MMP55BDDsm2226btm3bZuDAgUlSOU633nrrfOELX6hcynX77bfnzTffzFe/+tUP1Tv/WAYNGpTZs2dXXj/60Y+SpN73gDVx7mRD++d//ue88MIL+dWvfpUhQ4ZkypQp2WuvvSqXbn/Qd9GP6p0/A3V1dZk3b169Y/zd35eTt8/Xw4cPzw477JB27dpl++23T/J/5+EWLVrk8MMPr5yHZ8+enUceecSD3TYhH3Rcry25RLkJLPlQjjnmmFx//fW54YYbGvyQFf/v3iPvvgdgURQN5r3zZsurl60e4r82jjrqqMyaNSvjxo3LtGnTMnv27HTo0CHLly+v1BxxxBF56qmnMn369EyYMCHbbbddgyfwsunabLPNGtwvZ8WKFfWmV61alR/84Af1fgF57LHH8uc//zktW7ZM165d8+STT+Y///M/06pVq4wcOTL77LNPVqxY8Z4/D+/0t7/9LQcddFB23XXX/OIXv8isWbPyn//5nw16eef/5K677rocffTR77tdym+nnXbKNttsk8mTJ2fy5MkZMGBAkrfv/7f99tvn/vvvz+TJk/P5z38+q1atSpMmTTJr1qx6x+LcuXMr9zB797H8Xt59o/uqqqrKuXf1f3/zm9/Ue58nnniich/LAw88MH/7298yatSovPDCC9l3330rl4atTQ+33HJLTj311BxzzDG58847M3v27Bx99NH1zt2dOnXKwQcfnOuuuy4LFizIHXfc4UvdP6j3+y6wNufoJA3CmLZt2+aPf/xjfvazn2XrrbfOeeedl9133z2vvfbaWh2jr7/+evbff/9svvnmmTBhQmbOnFm5VPGdx+lxxx2XSZMmZenSpbnuuuvyta99rV7gxKanTZs22WmnnSqv1b/4flBg6NzJx6Fly5YZPHhwzjvvvEybNi1HHXVUvv/976/1d9E1qaqqWqfz9No4+OCD88orr+Tqq6/OAw88kAceeCBJw/PwXXfdleeffz7XXntt9t133wb3p+cf23sd15tt9nbM9c7j872OZ7lEuQks+VAOOOCALF++PMuXL8+QIUPqLdtpp53SvHnz3HfffZV5K1asyEMPPZSePXuu9Xv07Nmz8tfh1d49fe+99+bkk0/OQQcdlE996lNp0aJFXn755Xo1HTp0yBe/+MVcd911lZAHVuvYsWMWL15c76/H77wxc/L2w6aefPLJer+ArH6t/h9hq1atMmzYsPzoRz/KlClTMn369Dz22GPp2bNn3nrrrTz00EOV7T355JN57bXXKtMPPfRQ3nrrrVxyySXp27dvdt5557zwwgsNej388MPz7LPP5kc/+lHmzJmTI488cv1+GDSKQYMGZcqUKZkyZUplBFeSDBgwIL/73e8yY8aMDBo0KHvuuWdWrlyZBQsWNDgOVz9pdpdddvnA8+YH2WWXXdKiRYs8++yzDd6na9eulbqOHTvmqKOOyoQJEzJu3LhcddVVlfUfeeSRLF269D17uPfee9O/f/+MHDkye+65Z3baaac1PqRkdRh05ZVXZscdd6w3cp9NQ8eOHTN//vx6v2y8+xz9Xpo2bZr99tsvY8eOzaOPPlq5l/BOO+2UZs2a1TsuFy5cmD/96U+V6f/93//Nyy+/nIsvvjif+9zn8slPfnKNoz4POuigtGnTJldccUV++9vfCoZYZ86dNIZddtklr7/++lp9F23evHlWrlzZYBsdO3asd1++P//5z5UR7e+luro6W2+9db1j/K233qp3L+FXXnklc+fOzbnnnpt99903PXv2zMKFCxtsq1evXundu3euvvrq3Hzzzc7DVI7rjh07Jkm943Ntv0O8k1yi8TVt7AbYuDRp0qRyeXeTJk3qLWvTpk2++c1v5swzz0z79u3TrVu3jB07Nm+88UaOPfbYtX6PU045JUceeWR69+6dz372s5k4cWLmzJmTHXbYoVKz00475aabbkrv3r2zaNGinHnmmWnVqlWDbR133HEZOnRoVq5cKeShnj59+qR169b513/915x00kl58MEHG1xCcN5552Xo0KHp2rVrvvrVr2azzTbLo48+msceeywXXHBBrr/++qxcubKyrZtuuimtWrXKtttumw4dOuSAAw7I8ccfn6uuuipNmzbNqFGj6h2nO+64Y956661cfvnlOfjgg3P//ffnJz/5SYNet9xyy3z5y1/OmWeemf333z/bbLPNhv54+BgMGjQo3/rWt7JixYrKCMvk7cDym9/8Zt58880MGjQoXbt2zde//vUcccQRueSSS7Lnnnvm5Zdfzu9///v06tUrBx10UE4++eT0798/Y8eOzRe/+MXceeedqa2t/VD9tG3bNmeccUZOPfXUrFq1Kp/97GezaNGiTJs2LZtvvnmOPPLInHfeedl7773zqU99KsuWLcvtt99e+YPU8OHDc8455+TYY4/Nueeem2eeeabBk5R32mmn3Hjjjfnd736X7bffPjfddFNmzpxZudRrtSFDhqS6ujoXXHBBzj///HX8hNmYDRw4MC+99FLGjh2br3zlK6mtrc1vf/vbtGvX7n3Xu/322/PUU09ln332yZZbbpk77rgjq1atSo8ePbL55pvn2GOPzZlnnpkOHTqkc+fOOeeccyp/gEqSbt26pXnz5rn88stz4okn5vHHH8+//du/NXifJk2a5KijjsrZZ5+dnXbaaY2X8MLacO5kQ3rllVfy1a9+Ncccc0x22223tG3bNg899FDGjh2bQw45ZK2+i2633XZZsmRJ7rnnnsrtC1q3bp3Pf/7zGT9+fPr27ZtVq1blO9/5ToMrOdbklFNOycUXX5zu3bunZ8+eufTSS+v9QX/LLbdMhw4dctVVV2XrrbfOs88+m+9+97tr3NZxxx2Xb3/722ndunW+9KUvfaTPio3HBx3XrVq1St++fXPxxRdnu+22y8svv5xzzz33Q7+PXKIEGuXOmWxUVj90572sfuhOURTF0qVLi5NOOqnYaqutihYtWhSf+cxnigcffLBSu/rmtgsXLqzMe/jhh4skxdNPP12Zd+GFFxZbbbVVsfnmmxdHHnlkcdZZZ9W7ue0f//jHonfv3kWLFi2K7t27F//93/9dbLvttg0eZrJq1api2223LQ466KCP8Anwj+C9HrKz0047FS1btiyGDh1aXHXVVcW7T4u1tbVF//79i1atWhXt2rUrPv3pTxdXXXVVZf0+ffoU7dq1K9q0aVP07du33o2b582bV3zhC18oWrRoUXTr1q248cYbGxynl156abH11lsXrVq1KoYMGVLceOONDX5GiqIo7rnnniJJccstt6zXz4XGs/qG4J/85CfrzX/uueeKJMWOO+5Ymbd8+fLivPPOK7bbbruiWbNmRU1NTfGlL32pePTRRys111xzTbHNNtsUrVq1Kg4++ODi3//93xs8dOeDHmKyatWq4j/+4z+KHj16FM2aNSs6duxYDBkypJg6dWpRFEXxb//2b0XPnj2LVq1aFe3bty8OOeSQ4qmnnqqsP3369GL33XcvmjdvXuyxxx7FL37xi3o3PX/zzTeLo446qqiuri622GKL4pvf/Gbx3e9+d403L//e975XNGnSpHjhhRc+5CdLWXzQQ3fe72b4RfH2g0e6du1atGnTpjjiiCOKCy+8sMFDd979/eTee+8tBgwYUGy55ZZFq1atit12263eQxkWL15cHH744UXr1q2Lzp07F2PHji0GDBhQ76E7N998c7HddtsVLVq0KPr161f86le/WuMDUP76178WSSoPFmTT9V7fld99bK2Wdz2sxLmTDeXNN98svvvd7xZ77bVXUV1dXbRu3bro0aNHce655xZvvPFGURRr9130xBNPLDp06FAkKb7//e8XRVEUf//734v999+/aNOmTdG9e/fijjvuWONDd9597lyxYkVxyimnFO3atSu22GKL4rTTTiuOOOKIej9Dd911V9GzZ8+iRYsWxW677VZMmTJljQ/5Wbx4cdG6deti5MiR6/mTo8zW5rh+4oknir59+xatWrUq9thjj+LOO+9c40N35BLlVlUUa3njK9gIvfHGG+nSpUuuvfbafPnLX27sdmCdTZw4MaecckpeeOGFeg+YgH9Uxx9/fF588cX86le/auxWYI3uv//+DBw4MM8//3w6d+7c2O1AEudONi3PPfdctttuu8ycOTN77bVXY7cD70kusW5cEs4/pFWrVmX+/Pm55JJLUl1dnWHDhjV2S7BO3njjjTz99NO56KKLcsIJJwgr+YdXV1eXmTNnZuLEifmf//mfxm4HGli2bFmee+65fO9738uhhx4qrKQUnDvZlKxYsSLz5s3Ld7/73fTt21dYSWnJJT4aD93hH9Kzzz6bT3ziE7nlllty7bXXpmlT2Twbp7Fjx2aPPfZI586dc/bZZzd2O7DBHXLIIRk2bFhOOOGEDB48uLHbgQZ+9rOfpUePHqmrq8vYsWMbux1I4tzJpuX+++/Ptttum1mzZq3x/u9QFnKJj8Yl4QAAAABAaRhhCQAAAACUhsASAAAAACgNgSUAAAAAUBoCSwAAAACgNASWAAA0uoEDB2bUqFHrvP4zzzyTqqqqzJ49e731BABA4/BMdQAAGt0vf/nLNGvWrLHbAACgBASWAAA0uvbt2zd2CwAAlIRLwgEAaHTvvCR8u+22y5gxY3LMMcekbdu26datW6666qp69Q8++GD23HPPtGzZMr17987DDz/cYJtPPPFEDjrooGy++ebp3LlzRowYkZdffjlJMmXKlDRv3jz33ntvpf6SSy7JVlttlXnz5m24HQUA4AMJLAEAKJ1LLrmkEkSOHDky3/zmN/O///u/SZLXX389Q4cOTY8ePTJr1qyMHj06Z5xxRr31582blwEDBmSPPfbIQw89lNra2rz44os59NBDk/xfQDpixIjU1dXlkUceyTnnnJOrr746W2+99ce+vwAA/B+XhAMAUDoHHXRQRo4cmST5zne+k8suuyxTpkzJJz/5yUycODErV67Mtddem9atW+dTn/pUnn/++Xzzm9+srH/FFVdkr732ypgxYyrzrr322nTt2jV/+tOfsvPOO+eCCy7I3XffnW984xuZM2dORowYkS996Usf+74CAFCfwBIAgNLZbbfdKv+uqqpKTU1NFixYkCSZO3dudt9997Ru3bpS069fv3rrz5o1K5MnT87mm2/eYNt//etfs/POO6d58+aZMGFCdtttt2y77bYZN27chtkZAAA+FIElAACl8+4nhldVVWXVqlVJkqIoPnD9VatW5eCDD84Pf/jDBsveecn3tGnTkiSvvvpqXn311bRp0+ajtA0AwHrgHpYAAGxUdtlllzzyyCNZunRpZd6MGTPq1ey1116ZM2dOtttuu+y00071XqtDyb/+9a859dRTc/XVV6dv37454ogjKqEoAACNR2AJAMBGZfjw4dlss81y7LHH5oknnsgdd9yRf//3f69X861vfSuvvvpqDjvssDz44IN56qmncuedd+aYY47JypUrs3LlyowYMSL7779/jj766Fx33XV5/PHHc8kllzTSXgEAsJrAEgCAjcrmm2+eX//613niiSey55575pxzzmlw6XeXLl1y//33Z+XKlRkyZEh23XXXnHLKKamurs5mm22WCy+8MM8880yuuuqqJElNTU1++tOf5txzz83s2bMbYa8AAFitqlibmwABAAAAAHwMjLAEAAAAAEpDYAkAAAAAlIbAEgAAAAAoDYElAAAAAFAaAksAAAAAoDQElgAAAABAaQgsAQAAAIDSEFgCAAAAAKUhsAQAAAAASkNgCQAAAACUhsASAAAAACgNgSUAAAAAUBr/P4k+1nZ3yR+SAAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 1600x500 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(16,5))\n",
    "sns.barplot(x='index',y='number',data=day)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "id": "9b19cbb9-a383-4dac-a235-cb1a4fbbe247",
   "metadata": {},
   "outputs": [],
   "source": [
    "fire=data[data['year']==2015].groupby('month_new')['number'].sum().reset_index()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "id": "6fe5573e-f9c6-4070-b509-9d579e1095a7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>month_new</th>\n",
       "      <th>number</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>april</td>\n",
       "      <td>2573.000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>august</td>\n",
       "      <td>4363.125</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>dec</td>\n",
       "      <td>4088.522</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>jan</td>\n",
       "      <td>4635.000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>july</td>\n",
       "      <td>4364.392</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>jun</td>\n",
       "      <td>3260.552</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>march</td>\n",
       "      <td>2202.000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>may</td>\n",
       "      <td>2384.000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>nov</td>\n",
       "      <td>4034.518</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>oct</td>\n",
       "      <td>4499.525</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>sep</td>\n",
       "      <td>2494.658</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   month_new    number\n",
       "0      april  2573.000\n",
       "1     august  4363.125\n",
       "2        dec  4088.522\n",
       "3        jan  4635.000\n",
       "4       july  4364.392\n",
       "5        jun  3260.552\n",
       "6      march  2202.000\n",
       "7        may  2384.000\n",
       "8        nov  4034.518\n",
       "9        oct  4499.525\n",
       "10       sep  2494.658"
      ]
     },
     "execution_count": 99,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fire"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "id": "86990b1f-0831-427f-8e83-d355c0f0311c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: xlabel='month_new', ylabel='number'>"
      ]
     },
     "execution_count": 101,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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7LBDmjZtmgEDBuS1116r1mfRokUZNGhQqqqqUlVVlUGDBuWtt97axEcHAAAAAGyoWg0s33777XTr1i033HDDOtdfc801GTFiRG644YZMmzYtbdu2zaGHHpqlS5dW+gwZMiR33313xo0bl8ceeyzLli3LUUcdlVWrVlX6DBw4MDNmzMj48eMzfvz4zJgxI4MGDdrkxwcAAAAAbJj6tfnmRx55ZI488sh1riuXy7n++utz6aWX5rjjjkuSjB49Om3atMnYsWNz9tlnZ/Hixbntttty55135pBDDkmSjBkzJu3bt8+DDz6Yww8/PDNnzsz48ePz5JNPplevXkmSUaNGpXfv3pk1a1b22muvzXOwAAAAAMDHKuw9LOfMmZP58+fnsMMOq7Q1atQoffv2zRNPPJEkmT59et59991qfdq1a5fOnTtX+kyePDlVVVWVsDJJDjjggFRVVVX6rMuKFSuyZMmSai8AAAAAYNMqbGA5f/78JEmbNm2qtbdp06aybv78+WnYsGG23377j+zTunXrtfbfunXrSp91ueqqqyr3vKyqqkr79u0/0fEAAAAAAB+vsIHlGqVSqdpyuVxeq+2DPthnXf0/bj+XXHJJFi9eXHnNnTt3AysHAAAAADZUYQPLtm3bJslasyAXLFhQmXXZtm3brFy5MosWLfrIPq+//vpa+3/jjTfWmr35fo0aNUqLFi2qvQAAAACATauwgeWuu+6atm3bZuLEiZW2lStXZtKkSenTp0+SpEePHmnQoEG1PvPmzcsLL7xQ6dO7d+8sXrw4U6dOrfSZMmVKFi9eXOkDAAAAABRDrT4lfNmyZXn55Zcry3PmzMmMGTPSsmXL/J//838yZMiQDB8+PB07dkzHjh0zfPjwbLvtthk4cGCSpKqqKqeffnouuuiitGrVKi1btszFF1+cLl26VJ4a3qlTpxxxxBE588wzc/PNNydJzjrrrBx11FGeEA4AAAAABVOrgeVTTz2Vgw8+uLJ84YUXJklOOeWU3HHHHRk6dGiWL1+e8847L4sWLUqvXr0yYcKENG/evLLNddddl/r16+f444/P8uXL079//9xxxx2pV69epc9dd92V888/v/I08QEDBuSGG27YTEcJAAAAAKyvWg0s+/Xrl3K5/KHrS6VShg0blmHDhn1on8aNG2fkyJEZOXLkh/Zp2bJlxowZ80lKBQAA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5Prrr6+2vnv37hk2bNg6t/385z+fb37zm9XaFi5cmEaNGuV3v/vdJqiWj7KhY1kqlXLrrbfm2GOPzbbbbpuOHTvm17/+9eYruA7o169fBg8enCFDhmT77bdPmzZtcsstt+Ttt9/O17/+9TRv3jy77757HnjggSTJqlWrcvrpp2fXXXdNkyZNstdee+XHP/5xtX2uGeerrroq7dq1y5577pkkee2113LCCSekZcuWadq0aXr27JkpU6ZU2/bOO+9Mhw4dUlVVlRNOOCFLly7dPD+IrdDGHtvf//73adCgQebPn1/tfS666KIcdNBBm/XY6pp+/frl/PPPz9ChQ9OyZcu0bdu22mflq6++mi996Utp1qxZWrRokeOPPz6vv/56kmTWrFkplUp56aWXqu1zxIgR6dChg1nvtWDFihU5//zz07p16zRu3Dif/exnM23atMr6F198MV/84hfTokWLNG/ePJ/73Ocye/Zs13gF8GHX30ly++23p1OnTmncuHH23nvv/OQnP6lstz4ZztZIYLmVevvtt3PhhRdm2rRpeeihh7LNNtvk2GOPzerVqyt9vv3tb+eiiy7KM888kz59+mTAgAFZuHBhtf0MHTo0V111VWbOnJmuXbtu7sPYaq3P+HyUxx9/POecc06+9a1vZcaMGTn00EPzgx/8YINqmDdvXk488cScdtppmTlzZh555JEcd9xxKZfLufjii3P88cfniCOOyLx58zJv3rz06dOnJodK/n6uPfzww7n77rszYcKEPPLII5k+fXpl/de//vU8/vjjGTduXJ577rl85StfyRFHHJE//elPSf4eWPfv3z+f/vSnM3ny5Dz22GM5+uijs2rVqto6pDpvfc/hSy+9NBdffHFmzJiRPffcMyeeeGLee++9WqqamjjjjDMyduzYrFixotJ21113pV27djn44INrsTLW1xVXXJHjjz8+zz33XL7whS/kpJNOyptvvlnbZW1VRo8enR122CFTp07N4MGDc+655+YrX/lK+vTpk6effjqHH354Bg0alHfeeSerV6/OLrvskl/84hf5wx/+kH/5l3/JP//zP+cXv/hFtX0+9NBDmTlzZiZOnJj77rsvy5YtS9++ffPXv/41v/71r/Pss89m6NCh1T53Z8+enXvuuSf33Xdf7rvvvkyaNClXX3315v5xbFU25tgedNBB2W233XLnnXdW9v/ee+9lzJgx+frXv15bh1hnjB49Ok2bNs2UKVNyzTXX5Pvf/34mTpyYcrmcY445Jm+++WYmTZqUiRMnZvbs2fnqV7+aJNlrr73So0eP3HXXXdX2N3bs2AwcODClUqk2DqdOGzp0aH75y19m9OjRefrpp7PHHnvk8MMPz5tvvpm//OUvOeigg9K4ceP87ne/y/Tp03Paaaflvffec41Xyz7q+nvUqFG59NJL84Mf/CAzZ87M8OHD873vfS+jR4+uto/1yXC2KmXqhAULFpSTlJ9//vnynDlzyknKV199dWX9u+++W95ll13KP/zhD8vlcrn88MMPl5OU77nnnmr7ufzyy8vdunWrLJ9yyinlL33pS5vjELZq7x+fNT/7RYsWVdY/88wz5STlOXPmlMvlcvmrX/1q+Ytf/GK1fZx00knlqqqqyvK6xuZb3/pWuW/fvuVyuVyePn16OUn5lVdeWWdNxnbjWLp0ablhw4blcePGVdoWLlxYbtKkSflb3/pW+eWXXy6XSqXyX/7yl2rb9e/fv3zJJZeUy+Vy+cQTTywfeOCBm7Vu1vZR58T7z+FyuVz5nL311lsrfV588cVykvLMmTM3R7m8z/vH7lOf+lT5uuuuq7a+W7du5csvv7yynKR89913l8vlcvlvf/tbuWXLluWf//znlfXdu3cvDxs2bBNXzbrUZCwvu+yyyvKyZcvKpVKp/MADD2yGauuGvn37lj/72c9Wlt97771y06ZNy4MGDaq0zZs3r5ykPHny5HXu47zzzit/+ctfriyfcsop5TZt2pRXrFhRabv55pvLzZs3Ly9cuHCd+7j88svL2267bXnJkiWVtm9/+9vlXr161fjY6rpNMbY//OEPy506daos33PPPeVmzZqVly1btgmOgDU+OJblcrm83377lb/zne+UJ0yYUK5Xr1751Vdfraxb8zvL1KlTy+VyuTxixIjybrvtVlk/a9ascpLyiy++uHkOgIply5aVGzRoUL7rrrsqbStXriy3a9eufM0115QvueSS8q677lpeuXLlOrd3jVd7Pur6u3379uWxY8dWa/vXf/3Xcu/evcvlcnm9MpytkRmWW6nZs2dn4MCB2W233dKiRYvsuuuuSf4+3X+N3r17V/5dv3799OzZMzNnzqy2n549e26eguuY9RmfjzJr1qzsv//+1do+uPxxunXrlv79+6dLly75yle+klGjRvmK8SYwe/bsrFy5str51rJly+y1115Jkqeffjrlcjl77rln5R6xzZo1y6RJkypfMV4zw5LiWN9z+P0z03faaackyYIFCzZfoXxijRo1yte+9rX89Kc/TfL38/HZZ5/NqaeeWruFsd7efx42bdo0zZs3dx5uZO//GderVy+tWrVKly5dKm1t2rRJ8o/Pv5tuuik9e/bMjjvumGbNmmXUqFFrfX526dKl2n0rZ8yYkX333TctW7b80Do6dOiQ5s2bV5Z32mknY/0JbeyxPfXUU/Pyyy/nySefTJL89Kc/zfHHH5+mTZtujsOp0z74bbk158fMmTPTvn37tG/fvrJun332yXbbbVe5NjzhhBPy5z//uTJud911V7p375599tln8x0ASf7+O+i7776bAw88sNLWoEGD7L///pk5c2ZmzJiRz33uc2nQoEEtVsm6fNj19xtvvJG5c+fm9NNPr3Y9eOWVV1a75VSyfhnO1sRDd7ZSRx99dNq3b59Ro0alXbt2Wb16dTp37pyVK1d+5HYfnNLvl4dN46PGZ81Djcrvux/Mu+++W237crm81liVP3D/mG222Wattvfvp169epk4cWKeeOKJTJgwISNHjsyll16aKVOmVMIXPrkPjsEHrV69OvXq1cv06dNTr169auvW/LfQpEmTTVYfNbO+n7Hv/2VxzTm7vrd+YNP4uM/GdTnjjDPSvXv3vPbaa/npT3+a/v3751Of+tSmLJP1sL5j+cGLtlKp5DzcyNb1M/6wz79f/OIXueCCC3Lttdemd+/ead68eX70ox+tdS/KD/4Ouj7/X2isN76NPbatW7fO0Ucfndtvvz277bZb7r///q3+HmxF8WHnx7quK5Lq1xs77bRTDj744IwdOzYHHHBAfvazn+Xss8/eLHVT3Zr/31vXtWCpVHLdUGAfdv39m9/8Jsnfn1HRq1evtbb5OFvzbRnMsNwKLVy4MDNnzsxll12W/v37p1OnTuucObfmL2TJ3+8fM3369Oy9996bs9Q66ePGZ8cdd0zy93tcrDFjxoxq+9h7770zderUam1PPfVUteUdd9yx2j7WtZ9SqZQDDzwwV1xxRZ555pk0bNgwd999d5KkYcOG7pG4Eeyxxx5p0KBBtfNt0aJF+eMf/5gk2XfffbNq1aosWLAge+yxR7VX27Ztk/z9L+IPPfRQrdTP2tb3M5Zi+uBn45IlSzJnzpyP3KZLly7p2bNnRo0albFjx+a0007b1GWyHmoyltS+Rx99NH369Ml5552XfffdN3vsscdaM0jWpWvXrpkxY4b7jxbY+o7tGWeckXHjxuXmm2/O7rvvXm2mGJvfPvvsk1dffTVz586ttP3hD3/I4sWL06lTp0rbSSedlJ///OeZPHlyZs+enRNOOKE2yq3z9thjjzRs2DCPPfZYpe3dd9/NU089lU6dOqVr16559NFHP/SPsa7xate6rr8ff/zx7Lzzzvnv//7vta4HPziRqK5lOALLrdD222+fVq1a5ZZbbsnLL7+c3/3ud7nwwgvX6vd//+//zd13352XXnop3/jGN7Jo0SIXYZvBx43PHnvskfbt22fYsGH54x//mP/6r/9a66nSgwcPzv33358RI0bkT3/6U26++eY88MAD1f668vnPfz5PPfVU/t//+3/505/+lMsvvzwvvPBCZf2UKVMyfPjwPPXUU3n11Vfzq1/9Km+88UblF5MOHTrkueeey6xZs/I///M/HzsDiXVr1qxZTj/99Hz729/OQw89lBdeeCGnnnpqttnm7x+/e+65Z0466aScfPLJ+dWvfpU5c+Zk2rRp+eEPf5j7778/SXLJJZdk2rRpOe+88/Lcc8/lpZdeyo033pj/+Z//qc1Dq7PW9zOWYvr85z+fO++8M48++mheeOGFnHLKKev11+szzjgjV199dVatWpVjjz12M1TKx6npWFK79thjjzz11FP57W9/mz/+8Y/53ve+V+3pth/mxBNPTNu2bXPMMcfk8ccfz3//93/nl7/8ZSZPnrwZqmZ9rO/YHn744amqqsqVV17pYTsFcMghh6Rr16456aST8vTTT2fq1Kk5+eST07dv32q3BzvuuOOyZMmSnHvuuTn44IOz884712LVdVfTpk1z7rnn5tvf/nbGjx+fP/zhDznzzDPzzjvv5PTTT883v/nNLFmyJCeccEKeeuqp/OlPf8qdd96ZWbNmJXGNV5s+6vp72LBhueqqq/LjH/84f/zjH/P888/n9ttvz4gRI6rto65lOALLrdA222yTcePGZfr06encuXMuuOCC/OhHP1qr39VXX50f/vCH6datWx599NHce++92WGHHWqh4rrl48anQYMG+dnPfpaXXnop3bp1yw9/+MNceeWV1fZx4IEH5qabbsqIESPSrVu3jB8/PhdccEEaN25c6XP44Yfne9/7XoYOHZr99tsvS5cuzcknn1xZ36JFi/z+97/PF77whey555657LLLcu211+bII49Mkpx55pnZa6+9KvchevzxxzfxT2br9aMf/SgHHXRQBgwYkEMOOSSf/exn06NHj8r622+/PSeffHIuuuii7LXXXhkwYECmTJlSuZfQnnvumQkTJuTZZ5/N/vvvn969e+fee+9N/fru6lEb1vczlmK65JJLctBBB+Woo47KF77whRxzzDHZfffdP3a7E088MfXr18/AgQOrfdZSe2o6ltSuc845J8cdd1y++tWvplevXlm4cGHOO++8j92uYcOGmTBhQlq3bp0vfOEL6dKlS66++mohdYGs79hus802OfXUU7Nq1apqv5tSO0qlUu65555sv/32Oeigg3LIIYdkt912y89//vNq/Vq0aJGjjz46zz77bE466aRaqpbk79fxX/7ylzNo0KB85jOfycsvv5zf/va3lT+q/+53v8uyZcvSt2/f9OjRI6NGjarcEsA1Xu35qOvvM844I7feemvuuOOOdOnSJX379s0dd9yx1gzLupbhlMofd4M1tjqvvPJKdt111zzzzDPp3r17bZfDRnLmmWfmpZdeyqOPPlrbpcBW6cQTT0y9evUyZsyY2i6FDbQxxm7u3Lnp0KFDpk2bls985jMbsTo2hPMQtg5nnnlmXn/99fz617+u7VIACq+uZjhmWMIW6t/+7d/y7LPP5uWXX87IkSMzevTonHLKKbVdFmx13nvvvfzhD3/I5MmT8+lPf7q2y2EDbIyxe/fdd/Pqq6/mO9/5Tg444ABhZS1xHsLWYfHixXnwwQdz1113ZfDgwbVdDgAFJrCELdTUqVNz6KGHpkuXLrnpppvy7//+7znjjDNquyzY6rzwwgvp2bNnPv3pT+ecc86p7XLYABtj7B5//PF86lOfyvTp03PTTTdt5ApZX85D2Dp86UtfyoABA3L22Wfn0EMPre1yACgwXwkHAAAAAArDDEsAAAAAoDAElgAAAABAYQgsAQAAAIDCEFgCAAAAAIUhsAQAYIs1bNiwdO/evbbLAABgIxJYAgCwRSiVSrnnnntquwwAADYxgSUAAAAAUBgCSwAANki/fv0yePDgDBkyJNtvv33atGmTW265JW+//Xa+/vWvp3nz5tl9993zwAMPVLaZNGlS9t9//zRq1Cg77bRTvvvd7+a9996rts/zzz8/Q4cOTcuWLdO2bdsMGzassr5Dhw5JkmOPPTalUqmyvMadd96ZDh06pKqqKieccEKWLl263sfyUe+bJIsXL85ZZ52V1q1bp0WLFvn85z+fZ599trKuXr16mT59epKkXC6nZcuW2W+//Srb/+xnP8tOO+20XvUAACCwBACgBkaPHp0ddtghU6dOzeDBg3PuuefmK1/5Svr06ZOnn346hx9+eAYNGpR33nknf/nLX/KFL3wh++23X5599tnceOONue2223LllVeutc+mTZtmypQpueaaa/L9738/EydOTJJMmzYtSXL77bdn3rx5leUkmT17du65557cd999ue+++zJp0qRcffXVG3QsH/a+5XI5X/ziFzN//vzcf//9mT59ej7zmc+kf//+efPNN1NVVZXu3bvnkUceSZI899xzlf9dsmRJkuSRRx5J3759a/aDBgCogwSWAABssG7duuWyyy5Lx44dc8kll6RJkybZYYcdcuaZZ6Zjx475l3/5lyxcuDDPPfdcfvKTn6R9+/a54YYbsvfee+eYY47JFVdckWuvvTarV6+u7LNr1665/PLL07Fjx5x88snp2bNnHnrooSTJjjvumCTZbrvt0rZt28pykqxevTp33HFHOnfunM997nMZNGhQZbv18VHv+/DDD+f555/Pf/zHf6Rnz57p2LFj/u3f/i3bbbdd/vM//zPJ32dprgksH3nkkfTv3z+dO3fOY489Vmnr169fjX/WAAB1jcASAIAN1rVr18q/69Wrl1atWqVLly6VtjZt2iRJFixYkJkzZ6Z3794plUqV9QceeGCWLVuW1157bZ37TJKddtopCxYs+NhaOnTokObNm2/wduvzvtOnT8+yZcvSqlWrNGvWrPKaM2dOZs+eneTvgeWjjz6a1atXZ9KkSenXr1/69euXSZMmZf78+fnjH/9ohiUAwAaoX9sFAACw5WnQoEG15VKpVK1tTTi5evXqlMvlamFl8vevWr+/34ft8/0zMDeklvXZbn22X716dXbaaafKDMr322677ZIkBx10UJYuXZqnn346jz76aP71X/817du3z/Dhw9O9e/e0bt06nTp1Wu96AADqOoElAACb1D777JNf/vKX1YLLJ554Is2bN8/OO++83vtp0KBBVq1atanKXKfPfOYzmT9/furXr7/Wg37WWHMfyxtuuCGlUin77LNP2rVrl2eeeSb33Xef2ZUAABvIV8IBANikzjvvvMydOzeDBw/OSy+9lHvvvTeXX355Lrzwwmyzzfr/OtqhQ4c89NBDmT9/fhYtWrQJK/6HQw45JL17984xxxyT3/72t3nllVfyxBNP5LLLLstTTz1V6devX7+MGTMmffv2TalUyvbbb5999tknP//5z92/EgBgAwksAQDYpHbeeefcf//9mTp1arp165Zzzjknp59+ei677LIN2s+1116biRMnpn379tl33303UbXVlUql3H///TnooINy2mmnZc8998wJJ5yQV155pXKfziQ5+OCDs2rVqmrhZN++fbNq1SozLAEANlCpvOYGQgAAAAAAtcwMSwAAAACgMASWAABslV599dU0a9bsQ1+vvvpqbZcIAMA6+Eo4AABbpffeey+vvPLKh67v0KFD6tevv/kKAgBgvQgsAQAAAIDC8JVwAAAAAKAwBJYAAAAAQGEILAEAAACAwhBYAgAAAACFIbAEAAAAAApDYAkAAAAAFIbAEgAAAAAoDIElAAAAAFAY/x90JYKeLkHnogAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 1600x500 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(16,5))\n",
    "sns.barplot(x=\"month_new\",y=\"number\",data=fire)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "id": "be377e52-072d-4b18-9d1a-76eb14f8fc1d",
   "metadata": {},
   "outputs": [],
   "source": [
    "data8=data.groupby('state')['number'].mean().sort_values(ascending=False).reset_index()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "id": "75571d61-6c97-4df9-8624-d34d2f3f158c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>state</th>\n",
       "      <th>number</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Sao Paulo</td>\n",
       "      <td>213.896226</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Mato Grosso</td>\n",
       "      <td>203.479975</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Bahia</td>\n",
       "      <td>187.222703</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Piau</td>\n",
       "      <td>158.174674</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Goias</td>\n",
       "      <td>157.721841</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Minas Gerais</td>\n",
       "      <td>156.800243</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Tocantins</td>\n",
       "      <td>141.037176</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Amazonas</td>\n",
       "      <td>128.243218</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Ceara</td>\n",
       "      <td>127.314071</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>Paraiba</td>\n",
       "      <td>111.073979</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>Maranhao</td>\n",
       "      <td>105.142808</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>Pará</td>\n",
       "      <td>102.561272</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>Pernambuco</td>\n",
       "      <td>102.502092</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>Roraima</td>\n",
       "      <td>102.029598</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>Santa Catarina</td>\n",
       "      <td>101.924067</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>Amapa</td>\n",
       "      <td>91.345506</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>Rondonia</td>\n",
       "      <td>84.876272</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>Acre</td>\n",
       "      <td>77.255356</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>Rio</td>\n",
       "      <td>64.698515</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>Espirito Santo</td>\n",
       "      <td>27.389121</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20</th>\n",
       "      <td>Alagoas</td>\n",
       "      <td>19.271967</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21</th>\n",
       "      <td>Distrito Federal</td>\n",
       "      <td>14.899582</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>22</th>\n",
       "      <td>Sergipe</td>\n",
       "      <td>13.543933</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               state      number\n",
       "0          Sao Paulo  213.896226\n",
       "1        Mato Grosso  203.479975\n",
       "2              Bahia  187.222703\n",
       "3               Piau  158.174674\n",
       "4              Goias  157.721841\n",
       "5       Minas Gerais  156.800243\n",
       "6          Tocantins  141.037176\n",
       "7           Amazonas  128.243218\n",
       "8              Ceara  127.314071\n",
       "9            Paraiba  111.073979\n",
       "10          Maranhao  105.142808\n",
       "11              Pará  102.561272\n",
       "12        Pernambuco  102.502092\n",
       "13           Roraima  102.029598\n",
       "14    Santa Catarina  101.924067\n",
       "15             Amapa   91.345506\n",
       "16          Rondonia   84.876272\n",
       "17              Acre   77.255356\n",
       "18               Rio   64.698515\n",
       "19    Espirito Santo   27.389121\n",
       "20           Alagoas   19.271967\n",
       "21  Distrito Federal   14.899582\n",
       "22           Sergipe   13.543933"
      ]
     },
     "execution_count": 106,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data8"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "id": "deb2c570-c1f3-4fe2-b33e-0797915e7d1f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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Dh06qGnTpqpUqZIMw9D27du1atUqzZs3T61btzY7YoLcvn1bhmEoderUkqRz585p1apVKlKkiGrVqmVyuueTIsWzTRC22WyKjo5O5jTJ70V97qCMTGaTJk3SkCFD1K1bN/uT0bZt2/TFF19o5MiR6t27t9kRE+TVV19Vvnz59NVXX9l/oO/fv6933nlHp0+f1q+//mpywsS7detWvC86ixcvblKixHnav0nlypWdlCTp9OrVS0FBQerUqZOio6NVpUoVbd++XalTp9aPP/6oqlWrmh3xufn4+CgkJER58+bVZ599pk2bNmndunXatm2bWrZsqfPnz5sdMUH8/Py0bt06lShRQkuWLNHQoUN14MABzZ8/X7Nnz9a+ffvMjpggrlyyRkdHa/LkyY99A37lyhWTkuFxQkNDNWXKFIeRGD179lTevHnNjoZ48O9lDdOmTdNHH32kdu3a6auvvlKHDh0UGhqq3bt3q2vXrho1apTZEROMktUabt26pe7du2v+/PmSpBMnTihPnjzq0aOH/P39NWjQIJMTJo2///5bx48fl81mU4ECBZQlSxazIyVI4cKF9e6778Z5nz9p0iR99dVXOnr0qEnJEqdWrVpq2rSp3nvvPV27dk2FChWSh4eH/vnnH02aNEnvv/++2RHxiBf+ucNAssqVK5cxf/78OMfnzZtn5MqVy4RESSNVqlTG0aNH4xw/cuSI4eXlZUKipHPp0iWjfv36RooUKeK9WZXNZotzs/p1Zc+e3di9e7dhGIaxatUqw9/f3zh+/Ljx0UcfGRUrVjQ5XcJ4e3sbJ06cMAzDMGrUqGFMmTLFMAzDOHfunJEqVSozoyVKqlSpjLCwMMMwDOPtt982Bg4caBjGg+tKkyaNmdESxdfX19i/f79hGIaxePFiI1++fEZkZKQxY8YMo2TJkianS5whQ4YY2bJlM8aPH2+kSpXK+PTTT41OnToZmTJlMqZOnWp2vAS7f/++MX78eKNcuXKGr6+vkSFDBoebVa1du9ZImTKlUb58eaN3795Gr169jPLlyxuenp7G+vXrzY6XKOfPnze++OILY+DAgUbv3r0dblblyv9eu3btMvr372+0aNHCaNKkicPNigoWLGgsWbLEMAzDSJs2rREaGmoYxoPnyK5du5oZLVGmTp1qpE2b1ujatauRMmVKo0uXLkaNGjUMHx8f48MP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SpW0unXrpnnz5ql+/frKli2bbDabw/nJkyeblCzxLly4oB9++CHen8FJkyaZlCpx7t27p3fffVdDhgxRnjx5zI6TrHbu3Knt27crX758atiwodlxkkTsiCBvb2+TkyTe6dOndePGDZUoUUJ37tzRgAED9Msvvyhv3ryaPHmycuXKZXbERHOlf68rV67ozp078vf3V0xMjCZMmKCtW7cqX758GjJkiDJkyGB2xAS5du2adu3apUuXLtlHScZq27atSanwOK70c/hv+X18+/ZtLVq0SMeOHbPPJGzTpo28vLzMjvbcUqRIofDwcGXNmtXh+F9//aWcOXMqKirKpGSJt3v3bn333XfxvuZduXKlSakSp1atWmrfvr1at26t9957T/v27VOPHj20cOFCXb16Vb///rvZEV0WZWQySJEiRZw32o8yDEM2m03R0dFOSpW0/Pz8tG7dOpUoUUJLlizR0KFDdeDAAc2fP1+zZ8/Wvn37zI6If4F9+/apXr16unXrliIjI5UxY0b9888/Sp06tbJmzarTp0+bHRH/J3PmzFqwYIHq1atndpQktXHjRjVs2FC5c+fW8ePHVaxYMfsHM6VLl9amTZvMjphg6dOnV0hIiEu/+cGLLTo6Wlu3blXx4sUtVR48izNnzuj+/fvKnz+/w/GTJ0/Kw8PDJUpWV7FmzRq1adNGkZGR8vb2dniNb7PZdOXKFRPTJc7Vq1c1Z84cHT16VDabTYULF1aHDh2UMWNGs6PhIfw+toYffvhBktS4cWPNnz9fPj4+9nPR0dHauHGjgoODdfz4cbMiJsrSpUvVtm1b1apVS8HBwapVq5ZOnjyp8PBwNWnSRN98843ZERNkz549unHjhqpVq6a///5b7dq1s3948c0331h2ObNY0dHRWrVqlcPzfKNGjeTubv6KjZSRyeB55t9XqVIlGZMkHy8vL504cUIBAQFq27at/P39NXbsWIWFhalIkSK6efOm2RGfS58+ffTpp58qTZo06tOnzxMfa9WRTpJrjCJ8WNWqVVWgQAHNnDlT6dOn14EDB+Th4aG33npLPXv2tPQaH9KDT4nv3bvncMyqo6n9/f31yy+/qECBAmZHSVLly5dXnTp1NGLECHl7e+vAgQPKmjWr2rRpozp16uj99983O2KCdejQQUFBQU99TrSi48eP6/PPP7e/MCtUqJC6d++uggULmh0tUVasWKHly5fH+xwfEhJiUqrESZUqlY4eParcuXObHSVJValSRR07dowz2n3RokX6+uuv9csvv5gTLIlcunQp3lGExYsXNylRwhUoUED16tXT6NGjXWJt9FhbtmxRo0aNlC5dOvt6znv37tW1a9f0ww8/WO49SkREhP010tNmqVnttZQr/j7+4YcfVLduXXl4eNhLvMexyqyF2HXDbTabHq1YYj9kmjhxoho0aGBGvEQrXry4unTpoq5du9pf8+bOnVtdunRRtmzZNHz4cLMjPjfDMBQWFqasWbNachTu0xw+fFiNGjVSeHi4/TXuiRMnlCVLFv3www8KCgoyNR9lJBKkQIECGjlypOrXr6/cuXNr6dKleu2113TgwAFVr17dcovKV6tWTatWrVL69Onti+bHx2azWXakkyuOIkyfPr1+//13FSxYUOnTp9eOHTtUuHBh/f7772rXrp2OHTtmdsTnFhkZqYEDB2r58uW6fPlynPNWHU09ceJEnT59WtOnT3/qyHEr8fb21v79+5U3b15lyJBBW7duVdGiRXXgwAE1atRIZ8+eNTtigo0aNUoTJkxQ9erVVaZMGaVJk8bhvBU/wJAeFHatWrVS2bJl7Qvj79y5U7t379aSJUv05ptvmpwwYaZNm6aPPvpI7dq101dffaUOHTooNDRUu3fvVteuXTVq1CizIyZIuXLlNHbsWFWvXt3sKEkqXbp0CgkJUb58+RyOnzp1SmXLltW1a9fMCZZIe/fuVbt27XT06NE4b8atOiMoTZo0OnTokMuNSitWrJgqVqyomTNnys3NTdKD1xgffPCBtm3bpsOHD5uc8Pm4ubnp4sWLypo162NnqVl1Zpor/j5+eCpzbIkXHyv+e+XOnVu7d++29PJe8UmTJo2OHDmiXLlyKXPmzNq8ebOCgoJ09OhRvfbaa7p48aLZEZ9bTEyMUqVKpSNHjsSZqeAKKlSooKxZs2r+/Pn2GSZXr15V+/btdenSJe3YscPUfOaPzXRxv/766xPPV65c2UlJklavXr3Upk0bpU2bVoGBgapataqkB9drdsOeEJs3b473z66kd+/eev311+2jCHfu3OkwitCKPDw87C82fX19FRYWpsKFC8vHx0dhYWEmp0uYAQMGaPPmzZoxY4batm2rL774Qv/73//05ZdfauzYsWbHS7CtW7dq8+bN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a2rGjBkO67VawcGDB/XJJ5889nzdunU1YcIEJyZKWq64w2qst956SxUrVlSTJk10+PBhLVy40OxIiVKvXj198sknqlu3brwjj4cOHWr/HWBFsRvLuSJXHrHganr27KnZs2erWrVq8U6RtSJ3d3e9//77Onr0qNlRktTjRsfcvHnTsq93JWns2LHq27evRo0apaCgoDhrRlp1yQrpwQi1+HarX716tTJlymRSKri6IUOGqF69elq+fLkuXryo9u3bO7zGXbVqlSpVqmRiwsRx1dfyvXv3loeHh8LCwhyWKGrRooV69+5t6TJSejA7d8WKFQoNDVX//v2VMWNGhYSEyNfXV9mzZzc1G9O08Vy+/PJL/fjjj1qzZo2kB1NJixYtat8h/NixYxowYIAl12Lp0KHDMz2OUa8vlitXrtjXhsyXL98LuTjvs3h0h989e/aoRIkS9jcHZ86cUaFChSxbirviDqvSgw9gYkfMhIWFqWHDhrLZbJo1a5YqVqxoyREzf/31l0qXLi03Nzd169ZNBQsWlM1m09GjR/XFF18oOjra/iLGym7duhVvaVe8eHGTEiXO00Ys8LvrxZIxY0YtWrTIsruqPk61atXUs2dPNW7c2OwoidanTx9J0tSpU9W5c2eHjcmio6P1+++/y83NTdu2bTMrYqLELlkR3/Rzqy9ZMW/ePHXq1El16tRx2K1+7dq1+vrrr9W+fXtzA8Jl/fHHHwoODpafn5/efPNNh6VhZs+erfLly1tqp+mHuepreT8/P61bt04lSpRwWKbtzJkzCgoK0s2bN82OmGAHDx5UjRo15OPjo7Nnz+r48ePKkyePhgwZonPnzmnBggWm5mNkJJ7L4sWL4xSNS5YssU8lXbRokb744gtLlpG8UbOmjBkzqnz58mbHSLSMGTMqNDTUXkbGbpwU6+TJk5YtWqUH13fjxg1JD6YBHz58WEFBQbp27Zql1855+PO8nDlzavv27WrTpo1q1qxpYqrEeXjk8eDBgx1GHteuXduSI48f9vfff6tDhw7673//G+95q74Bd9URC67Kx8fH/trJlXzwwQfq27evLly4EO8GUVYq+2PXcDYMQ4cOHXLYqCZlypQqUaKE+vXrZ1a8RHvSkhWx125V7du3V+HChTVt2jStXLlShmGoSJEi2rZtm1566SWz48GFFSlSxL5m5KPeffddJ6dJ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6IHuS0xMbOckRLqBxUgiIiIiIiIiIiLSiHufSSUiIiIiIuqEcnNz8c9//lNtLTk5GTY2NujduzfmzJmDuro6QemIiOhR3b17FwkJCfD19cWTTz4JZ2dnTJkyBcnJyZyGrgEsRhIRERERETWxatUqFBQUqD4uLCxESEgIJk6ciKioKGRmZuKdd94RmJCIiNpKqVRiypQpeO211/Djjz/C2dkZf/7zn1FeXo7AwEBMmzZNdMQOj9O0iYiIiIiImsjLy8OaNWtUH6ekpMDNzQ2ffPIJAGDgwIFYuXIlVq1aJSghERG1lVwux+HDh5GdnQ13d3e1azk5OfDz80NycjJmzZolKGHHx5ORRERERERETdy4cQN9+vRRfXzo0CF4eXmpPh4xYgQuXbokIhoRET2inTt34q233mpRiASA8ePHIyoqCjt27BCQrPNgMZKIiIiIiKiJPn36oLS0FADw22+/4ezZs3jmmWdU12/fvg0DAwNR8YiI6BEUFBSobTA15+3tjfz8fA0m6nxYjCQiIiIiImrCy8sLUVFROHLkCJYuXQoTExOMGTNGdb2goAB2dnYCExIRUVtVV1ernX5vrk+fPrhx44YGE3U+7BlJRERERETUxNq1a+Hv74+xY8fC1NQUSUlJMDQ0VF1PSEiAh4eHwIRERNRWCoUC+vr3Lofp6emhoaFBg4k6H4mSM8uJiIiIiIhaqKmpgampKfT09NTWq6urYWpqqlagJCIi3SCVSuHt7Q0jI6NWr9fV1SErKwsKhULDyToPFiOJiIiIiIiIiKhTCAoKeqD7EhMT2zlJ58ViJBEREREREREREWkEB9gQERERERERERGRRrAYSURERERERERERBrBYiQRERERERERERFpBIuRREREREREREREpBEsRhIREREREREREZFGsBhJREREREREREREGsFiJBEREREJFRgYCD8/v4f+vFWrVmHYsGGPPQ8RERERtR8WI4mIiIiIiIiIiEgjWIwkIiIiIo3YvXs3nJ2dYWxsDEtLS0ycOBGLFy9GUlISvvrqK0gkEkgkEhw8eBAAsGTJEjg4OMDExAS2traIjo5GfX09AEAulyMmJgb5+fmqz5PL5QCAmpoazJkzB71794a5uTnGjx+P/Px8QV81ERERETWlLzoAEREREXV8V65cwYwZM7Bx40ZMmzYNt2/fxpEjRzBr1ixUVFTg1q1bSExMBAD06NEDAGBmZga5XI5+/fqhsLAQs2fPhpmZGd58800EBATg3LlzyMrKwrfffgsAsLCwgFKphI+PD3r06IG9e/fCwsIC27Ztw4QJE3DhwgXV701EREREYrAYSURERETt7sqVK2hoaIC/vz9kMhkAwNnZGQBgbGyMuro69O3bV+1zli9frvq1tbU1IiIisGvXLrz55pswNjaGqakp9PX11T4vJycHhYWFuHbtGoyMjAAA7733HjIyMrB7927MmTOnvb9UIiIiIroPFiOJiIiIqN0NHToUEyZMgLOzMzw9PeHh4YEXXngB3bt3v+fn7N69G5s2bcLFixfx888/o6GhAebm5vf9c86cOYOff/4ZlpaWauu//vor/v3vfz+Wr4WIiIiI2o7FSCIiIiJqd3p6evjmm29w/Phx7N+/H1u2bMGyZcuQm5vb6v0nT57ESy+9hJiYGHh6esLCwgIpKSmIjY29759z9+5dWFlZqfpONtWtW7fH8JUQERER0aNgMZKIiIiINEIikWDUqFEYNWoUVqxYAZlMhvT0dBgaGkKhUKjde+zYMchkMixbtky1Vl5ernZPa583fPhwVFVVQV9fH9bW1u32tRARERFR27AYSURERETtLjc3F9nZ2fDw8EDv3r2Rm5uL//znP3jiiSdQW1uLffv2obi4GJaWlrCwsIC9vT0qKiqQkpKCESNG4Ouvv0Z6erra72ltbY3S0lLk5eVhwIABMDMzw8SJE/HMM8/Az88PGzZsgKOjIyorK7F37174+fnB1dVV0N8AEREREQGAVHQAIiIiIur4zM3NcfjwYUyePBkODg5Yvnw5YmNj4e3tjdmzZ8PR0RGurq7o1asXjh07hqlTp2LhwoWYP38+hg0bhuPHjyM6Olrt93z++efh5eUFd3d39OrVCzt37oREIsHevXvx7LPPIjg4GA4ODnjppZdQVlaGPn36CPrqiYiIiKiRRKlUKkWHICIiIiIiIiIioo6PJyOJiIiIiIiIiIhII1iMJCIiIiIiIiIiIo1gMZKIiIiIiIiIiIg0gsVIIiIiIiIiIiIi0ggWI4mIiIiIiIiIiEgjWIwkIiIiIiIiIiIijWAxkoiIiIiIiIiIiDSCxUgiIiIiIiIiIiLSCBYjiYiIiIiIiIiISCNYjCQiIiIiIiIiIiKNYDGSiIiIiIiIiIiINOK/4c/rFHnCR3gAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 1600x500 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(16,5))\n",
    "sns.barplot(x='state',y='number',data=data8)\n",
    "plt.xticks(rotation=90)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 113,
   "id": "50f56327-fe6a-431d-90ab-0a2bb3151432",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['Acre', 'Alagoas', 'Amapa', 'Amazonas', 'Bahia', 'Ceara',\n",
       "       'Distrito Federal', 'Espirito Santo', 'Goias', 'Maranhao',\n",
       "       'Mato Grosso', 'Minas Gerais', 'Pará', 'Paraiba', 'Pernambuco',\n",
       "       'Piau', 'Rio', 'Rondonia', 'Roraima', 'Santa Catarina',\n",
       "       'Sao Paulo', 'Sergipe', 'Tocantins'], dtype=object)"
      ]
     },
     "execution_count": 113,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[data['month_new']==\"dec\"]['state'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "64a44364-bb6f-46dc-bff3-f5fba854dfb1",
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
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
