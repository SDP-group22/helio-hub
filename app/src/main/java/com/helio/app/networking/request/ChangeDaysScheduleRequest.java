package com.helio.app.networking.request;

import com.helio.app.model.Day;

import java.util.ArrayList;
import java.util.List;

@SuppressWarnings({"FieldCanBeLocal", "unused", "RedundantSuppression", "MismatchedQueryAndUpdateOfCollection"})
public class ChangeDaysScheduleRequest {
    private final int id;
    private final List<String> days;

    public ChangeDaysScheduleRequest(int id, List<Day> days) {
        this.id = id;
        this.days = new ArrayList<>();
        for (Day d : days) {
            this.days.add(d.dayName);
        }
    }
}
