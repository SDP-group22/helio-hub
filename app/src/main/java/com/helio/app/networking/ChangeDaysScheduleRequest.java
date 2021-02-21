package com.helio.app.networking;

import com.helio.app.model.Day;

import java.util.List;

@SuppressWarnings({"FieldCanBeLocal", "unused", "RedundantSuppression"})
public class ChangeDaysScheduleRequest {
    private final int id;
    private final List<Day> days;

    public ChangeDaysScheduleRequest(int id, List<Day> days) {
        this.id = id;
        this.days = days;
    }
}
