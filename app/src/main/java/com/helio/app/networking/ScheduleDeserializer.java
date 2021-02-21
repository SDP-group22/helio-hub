package com.helio.app.networking;

import com.google.gson.Gson;
import com.google.gson.JsonDeserializationContext;
import com.google.gson.JsonDeserializer;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParseException;
import com.google.gson.reflect.TypeToken;
import com.helio.app.model.Day;
import com.helio.app.model.Schedule;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class ScheduleDeserializer implements JsonDeserializer<Schedule> {

    @Override
    public Schedule deserialize(JsonElement json, Type typeOfT, JsonDeserializationContext context) throws JsonParseException {
        Gson gson = new Gson();
        Schedule schedule = gson.fromJson(json, Schedule.class);

        // Get the element from the json
        JsonObject jsonObject = json.getAsJsonObject();
        JsonElement jsonElement = jsonObject.get("days");

        // Convert to type Day
        List<String> dayStrings = gson.fromJson(jsonElement, new TypeToken<List<String>>(){}.getType());
        List<Day> days = new ArrayList<>();
        for (String d : dayStrings) {
            days.add(Day.getEnumFromName(d));
        }
        schedule.setDays(days);

        return schedule;
    }
}