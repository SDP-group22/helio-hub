package com.helio.app.model;

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

    public final String dayName;

    Day(String dayName) {
        this.dayName = dayName;
    }

    /**
     * Gets a day enum from its string representation
     */
    public static Day getEnumFromName(String name) throws IllegalArgumentException {
        for (Day day : Day.values()) {
            if (name.equals(day.dayName)) {
                return day;
            }
        }
        throw new IllegalArgumentException("No enum constant " + name);
    }
}
