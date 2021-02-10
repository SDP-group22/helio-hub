package com.helio.app.model;

import java.util.HashMap;
import java.util.Map;

/**
 * Represents the day of the week. DayOfWeek already exists in Java, but only works in Android API level 26+
 */
public enum Day {

    MONDAY("Monday"),
    TUESDAY("Tuesday"),
    WEDNESDAY("Wednesday"),
    THURSDAY("Thursday"),
    FRIDAY("Friday"),
    SATURDAY("Saturday"),
    SUNDAY("Sunday");

    // Lookup map for getting a day from a String from the API
    private static final Map<String, Day> lookup = new HashMap<>();

    static {
        for (Day d : Day.values()) {
            lookup.put(d.dayName, d);
        }
    }

    public final String dayName;

    Day(String dayName) {
        this.dayName = dayName;
    }

    /**
     * Gets a day enum from its string representation
     */
    public static Day getEnumFromName(String name) throws IllegalArgumentException {
        return lookup.get(name);
    }
}
