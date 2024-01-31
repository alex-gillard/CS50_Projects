-- Keep a log of any SQL queries you execute as you solve the mystery.
-- Theft took place on July (numeric = 07) 28th on Humphrey Street
-- Finding description from crime_scene_reports
SELECT description
FROM crime_scene_reports
WHERE month = 7
AND day = 28
AND street = 'Humphrey Street';
-- Description inidicates that the theft of our precious duck took place 10:15am at Humphrey Street bakery.
-- Looking into the bakery security logs may prove beneficial.
-- Littering time: 16:36 (4:36pm)

-- Collect transcripts of relevent interviews
SELECT name, transcript
FROM interviews
WHERE month = 7
AND day = 28
AND name = 'Ruth' OR name = 'Eugene' OR name = 'Raymond'
AND transcript LIKE '%thief%';

-- Find license plate of thief exiting bakery within timeframe specified by Ruth
-- (10:15am - 10:25am)
SELECT license_plate, month, day, hour, minute, activity
FROM bakery_security_logs
WHERE month = 7
AND day = 28
AND hour = 10
AND minute >= 15 AND minute <= 25
AND activity = 'exit';

-- Find out bank account numbers of people visiting ATMs on Leggett Street
SELECT people.name, people.license_plate
FROM people
JOIN bank_accounts ON people.id = bank_accounts.person_id
JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
WHERE atm_transactions.month = 7
AND atm_transactions.day = 28
AND atm_transactions.atm_location = 'Leggett Street'
AND transaction_type = 'withdraw';

-- Matches between last two queries based on theft timeframe
-- Bruce, Diana, Iman, Luca
-- These are the people withdrawing money during the month and day of the theft

-- Get phone number of each person
SELECT name, phone_number
FROM people
WHERE name = 'Bruce' OR name = 'Diana' OR name = 'Iman' OR name = 'Luca';
-- Check phone calls for duration less than 1 min
SELECT caller, duration, receiver
FROM phone_calls
WHERE month = 7
AND day = 28
AND duration < 60;
-- Diana had a phone call for 49 seconds with (725) 555-3243 (Philip)
-- Bruce had a 45 second phone call with (375) 555-8161 (Robin)

-- Find out names of receivers
SELECT name, phone_number
FROM people
WHERE phone_number = '(725) 555-3243' OR phone_number = '(375) 555-8161';

-- Get passport number from each person suspected
SELECT passport_number, name
FROM people
WHERE name = 'Diana' OR name = 'Philip' OR name = 'Bruce' OR name = 'Robin';

-- Get flight information
SELECT destination_airport_id, origin_airport_id, hour, minute
FROM flights
WHERE month = 7
AND day = 29;
-- Earliest flight is 8:20am, destination id is 4
SELECT full_name, city
FROM airports
JOIN flights dest ON dest.destination_airport_id = airports.id
WHERE dest.destination_airport_id = 4;
-- 8:20am flight from Fiftyville Airport to LaGuardia Airport
SELECT passengers.passport_number
FROM passengers
JOIN flights ON passengers.flight_id = flights.id
WHERE flights.month = 7
AND flights.day = 29
AND flights.hour = 8
AND flights.minute = 20
AND flights.origin_airport_id = 8
AND flights.destination_airport_id = 4;

-- Bruce's passport number has shown up in the list of passport numbers associated with the earliest flight from Fiftyville to New York City
-- We know from previous information that Bruce called Robin, following the theft at the Bakery.
-- Therefore we can conclude the following:

-- Thief = Bruce
-- Accomplice = Robin
-- Escape Location = NY City




