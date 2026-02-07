-- shoes
INSERT INTO shoes (id, brand, full_name, retired, carbon_insert)
VALUES (1, 'ASICS', 'ASICS Gel Nimbus 26', 0);

-- main_log
INSERT INTO main_log (
  date,
  run_of_the_day,
  distance_km,
  duration_seconds,
  active_cal,
  elevation_gain_meter,
  avg_heart_rate_bpm,
  effort_level,
  feel_score,
  shoe_id
)
VALUES (
  '2025-03-08',
  1,
  6.84,
  3610,
  487,
  82,
  144,
  3,
  4,
  1
);

-- split_log
INSERT INTO split_log (
  date,
  run_of_the_day,
  split_index,
  distance_km,
  duration_seconds,
  avg_heart_rate_bpm
)
VALUES
('2025-03-08', 1, 1, 1.0, 364, 144),
('2025-03-08', 1, 2, 1.0, 349, 150);

-- weather_log
INSERT INTO weather_log (
    date,
    time,
    temp_celsius,
    humidity_pct,
    wind_speed_kph
)
VALUES
('2025-03-08', '14', 1.1, 37, 30.3);
