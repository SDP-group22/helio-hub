package com.helio.app.networking;

import com.helio.app.model.Schedule;

import org.jetbrains.annotations.NotNull;

import java.util.Map;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class ScheduleCallback implements Callback<Schedule> {
    private final Map<Integer, Schedule> schedules;

    public ScheduleCallback(Map<Integer, Schedule> schedules) {
        this.schedules = schedules;
    }

    private void updateLocalState(Schedule s) {
        schedules.put(s.getId(), s);
        System.out.println("Updated local state for " + s);
    }

    @Override
    public void onResponse(@NotNull Call<Schedule> call, Response<Schedule> response) {
        Schedule s = response.body();
        if(s != null) {
            System.out.println(call + " succeeded: " + s);
            updateLocalState(s);
        } else {
            System.out.println("Communication error");
        }
    }

    @Override
    public void onFailure(@NotNull Call<Schedule> call, @NotNull Throwable t) {
        System.out.println(call + " failed: " + t);
    }
}
