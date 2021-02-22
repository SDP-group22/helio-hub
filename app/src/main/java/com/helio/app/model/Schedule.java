package com.helio.app.model;

import com.google.gson.annotations.SerializedName;

import org.jetbrains.annotations.NotNull;

import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Objects;

public class Schedule extends IdComponent {
    @SerializedName("motor_ids")
    private final List<Integer> motorIds;
    private String name;
    private boolean active;
    private List<Day> days;
    @SerializedName("target-level")
    private int targetLevel;
    private int gradient;
    private String time;

    public Schedule(int id, String name, boolean active, List<Day> days, int targetLevel,
                    int gradient, List<Integer> motorIds, String time) {
        super(id);
        this.name = name;
        this.active = active;
        this.days = days;
        this.targetLevel = targetLevel;
        this.gradient = gradient;
        this.motorIds = motorIds;
        this.time = time;
    }

    /**
     * Create a schedule with the ID only, leaving everything else as default.
     */
    public Schedule(int id) {
        this(id, "", false, new ArrayList<>(), 0, 0, new ArrayList<>(), "");
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public boolean isActive() {
        return active;
    }

    public void setActive(boolean active) {
        this.active = active;
    }

    public List<Day> getDays() {
        return days;
    }

    public void setDays(List<Day> days) {
        this.days = days;
    }

    public int getTargetLevel() {
        return targetLevel;
    }

    public void setTargetLevel(int targetLevel) {
        this.targetLevel = targetLevel;
    }

    public int getGradient() {
        return gradient;
    }

    public void setGradient(int gradient) {
        this.gradient = gradient;
    }

    public List<Integer> getMotorIds() {
        return motorIds;
    }

    public String getTime() {
        return time;
    }

    /**
     * Set the time of this schedule
     *
     * @param hour   the hour of the day (24-hour)
     * @param minute the minute
     */
    public void setTime(int hour, int minute) {
        // Locale is set because it complains about that sometimes causing bugs
        this.time = String.format(Locale.US, "%02d:%02d", hour, minute);
    }

    public int getTimeHour() {
        return Integer.parseInt(Objects.requireNonNull(time).split(":")[0]);
    }

    public int getTimeMinute() {
        return Integer.parseInt(Objects.requireNonNull(time).split(":")[1]);
    }

    @NotNull
    @Override
    public String toString() {
        return "Schedule{" +
                "id='" + getId() + '\'' +
                ", name='" + name + '\'' +
                ", active=" + active +
                ", days=" + days +
                ", targetLevel=" + targetLevel +
                ", gradient=" + gradient +
                ", motorIds=" + motorIds +
                ", time='" + time + '\'' +
                '}';
    }
}
