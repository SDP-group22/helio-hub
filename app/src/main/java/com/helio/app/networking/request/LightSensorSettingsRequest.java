package com.helio.app.networking.request;

import com.helio.app.model.Day;

import java.util.List;

public class LightSensorSettingsRequest extends ScheduleSettingsRequest {
    public LightSensorSettingsRequest(String name, boolean active, List<Day> days, int targetLevel, int gradient, List<Integer> motorIds, String time) {
        super(name, active, days, targetLevel, gradient, motorIds, time);
    }
}
