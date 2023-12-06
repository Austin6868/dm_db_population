# How to Use this Tool

## Getting it to Run
- Clone this repository or just download zip

- Once you are in the terminal under the same directory(assuming you already know how to run python and have pip installed), run:

  ```pip install -r requirements.txt```

- Once you have modified the code based on your needs following the instructions in the code, run: 

  ```python fake_data_generator.py```

  OR

  ```python fake_data_generator.py```

  (whichever one works) Under the same directory.

## Additional Notes
- Faker is one of the most used tools in this code base, here are some [more advanced examples](https://faker.readthedocs.io/en/master/fakerclass.html#examples) if you wanna consider them, but you can always chatGPT:)
- Usually, when I do a typical id (auto-incrementing integer), I usually do it like the id in this scenario:

  ```python
  record = {
            'id': i,
            'userid': fake.random_int(min = 1, max = 500),
        }
  ```

- When you need to reference one foreign key for example, you can do it like the userid, generate a unique random number of that specific range:

  ```python
  record = {
      'roomnumber': fake.random_int(min = 1, max = 50),
      'hotelid': fake.unique.random_int(min = 1, max = 500),
      'size': fake.random_int(min = 500, max = 1000),
      'description': "'" + fake.paragraph(nb_sentences=3) + "'",
      'pricenight': generate_random_decimal(min_value=100, max_value=1000, decimal_places=2),
  }
  ```

- If you have an entity that has multiple primary keys, I found it helpful to generate unique pairs/triplets/etc... using find_combos() function like this: 

  ```python
  combos = find_combos(ranges=[(1, 500), (1, 500)])
  record = {
      'userid': combos[0],
      'bookingid': combos[1],
      'stars': fake.random_int(min = 1, max = 5),
      'content': "'" + fake.paragraph(nb_sentences=3) + "'",
  }
  ```

- If you ever wanted to generate start and end time that happen sequentially, do it like this: 
  ```python
  start_time, end_time = generate_random_start_end_times()
  record = {
      'id': i,
      'userid': fake.unique.random_int(min = 1, max = 500),
      'roomnumber': fake.random_int(min = 1, max = 50),
      'hotelid': fake.random_int(min = 1, max = 500),
      "starttime": "'" + start_time + "'",
      "endtime": "'" + end_time + "'",
  }
  ```

where userid and bookingid are both primary keys, where both of them have a range where they can be mutually unique.
