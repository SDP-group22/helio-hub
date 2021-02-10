package com.helio.app.model;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class DayTest {

    @Test
    void getEnumFromNameCorrectNameWorks() {
        Day day = Day.getEnumFromName("Monday");
        assertEquals(Day.MONDAY, day);
    }

    @Test
    void getEnumFromNameWrongNameThrows() {
        Assertions.assertThrows(IllegalArgumentException.class, () -> Day.getEnumFromName("wEdnESdAY"));
        Assertions.assertThrows(IllegalArgumentException.class, () -> Day.getEnumFromName("水曜日"));
    }
}