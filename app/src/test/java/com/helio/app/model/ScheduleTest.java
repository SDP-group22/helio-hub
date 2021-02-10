package com.helio.app.model;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class ScheduleTest {
    private Schedule schedule;

    @BeforeEach
    void before() {
        schedule = new Schedule(0);
    }

    @Test
    void setTimeCorrect() {
        schedule.setTime(16, 20);
        assertEquals("16:20", schedule.getTime(), "Time string is set in correct format");
    }

    @Test
    void setTimeNumberDigitPaddingCorrect() {
        schedule.setTime(6, 9);
        assertEquals("06:09", schedule.getTime(), "Time string is set in correct format when numbers are 1 digit. Nice.");
    }

    @Test
    void getTimeHour() {
        schedule.setTime(4, 20);
        assertEquals(4, schedule.getTimeHour());
    }

    @Test
    void getTimeMinute() {
        schedule.setTime(4, 20);
        assertEquals(20, schedule.getTimeMinute());
    }
}