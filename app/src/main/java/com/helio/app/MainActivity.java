package com.helio.app;

import android.os.Bundle;
import android.os.Handler;
import android.view.MenuItem;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.navigation.NavController;
import androidx.navigation.Navigation;
import androidx.navigation.ui.AppBarConfiguration;
import androidx.navigation.ui.NavigationUI;

import com.google.android.material.bottomnavigation.BottomNavigationView;
import com.helio.app.model.Day;
import com.helio.app.model.Motor;
import com.helio.app.model.Schedule;
import com.helio.app.networking.HubClient;
import com.helio.app.networking.request.ChangeDaysScheduleRequest;
import com.helio.app.networking.request.ChangeGradientScheduleRequest;
import com.helio.app.networking.request.ChangeTimeScheduleRequest;
import com.helio.app.networking.request.MoveMotorRequest;
import com.helio.app.networking.request.RegisterMotorRequest;
import com.helio.app.networking.request.RegisterScheduleRequest;
import com.helio.app.networking.request.RenameMotorRequest;
import com.helio.app.networking.request.RenameScheduleRequest;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.concurrent.atomic.AtomicInteger;

public class MainActivity extends AppCompatActivity {
    public static final int DELAY = 250;
    private int postTime = 0;
    private Map<Integer, Motor> motors;
    private Map<Integer, Schedule> schedules;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Passing each menu ID as a set of Ids because each
        // menu should be considered as top level destinations.
        AppBarConfiguration appBarConfiguration = new AppBarConfiguration.Builder(
                R.id.navigation_control, R.id.navigation_blinds, R.id.navigation_hub)
                .build();
        NavController navController = Navigation.findNavController(this, R.id.nav_host_fragment);

        // This makes the bar at the top change when you use the navigation (changes the title text)
        NavigationUI.setupActionBarWithNavController(this, navController, appBarConfiguration);

        // This makes the fragment change when you press the navigation buttons
        BottomNavigationView navView = findViewById(R.id.nav_view);
        NavigationUI.setupWithNavController(navView, navController);

        fetchState();
    }

    @Override
    public boolean onOptionsItemSelected(@NonNull MenuItem item) {
        // Navigate backwards when pressing back button in top app bar
        if (item.getItemId() == android.R.id.home) {
            onBackPressed();
        }
        return super.onOptionsItemSelected(item);
    }

    private void fetchState() {
        motors = new HashMap<>();
        HubClient client = new HubClient("http://10.0.2.2:4310/");
        testMotor(client);
        testSchedule(client);
    }

    private void testMotor(HubClient client) {
        RegisterMotorRequest registerMotorRequest = new RegisterMotorRequest(
                "bedroom",
                "1.2.3.4",
                false,
                0, 0, 0, "style");
        // use Handler to force the actions to happen in order
        Handler handler = new Handler();
        handler.postDelayed(() -> client.addMotor(motors, registerMotorRequest), postTime);

        // This is extremely bad
        AtomicInteger id = new AtomicInteger();

        postTime += DELAY;
        handler.postDelayed(() -> id.set(new ArrayList<>(motors.keySet()).get(0)), postTime);

        postTime += DELAY;
        handler.postDelayed(() -> client.activateMotor(motors, id.get()), postTime);

        postTime += DELAY;
        handler.postDelayed(() -> {
            RenameMotorRequest renameMotorRequest = new RenameMotorRequest(id.get(), "kitchen");
            client.renameMotor(motors, renameMotorRequest);
        }, postTime);

        postTime += DELAY;
        handler.postDelayed(() -> client.getMotor(motors, id.get()), postTime);

        postTime += DELAY;
        handler.postDelayed(() -> {
            MoveMotorRequest moveMotorRequest = new MoveMotorRequest(id.get(), 25);
            client.moveMotor(motors, moveMotorRequest);
        }, postTime);

        postTime += DELAY;
        handler.postDelayed(() -> client.startMotorCalibration(motors, id.get()), postTime);

        postTime += DELAY;
        handler.postDelayed(() -> client.stopMotorCalibration(motors, id.get()), postTime);

        postTime += DELAY;
        handler.postDelayed(() -> client.deactivateMotor(motors, id.get()), postTime);

        postTime += DELAY;
        handler.postDelayed(() -> client.deleteMotor(motors, id.get()), postTime);
    }

    private void testSchedule(HubClient client) {
        int delay = 2000;
        schedules = new HashMap<>();
        List<Integer> motorIds = new ArrayList<>();
        motorIds.add(999);
        List<Day> days = new ArrayList<>();
        days.add(Day.MONDAY);
        RegisterScheduleRequest registerScheduleRequest = new RegisterScheduleRequest(
                "name",
                false,
                days,
                0, 0, motorIds, "16:20");

        // use Handler to force the actions to happen in order
        Handler handler = new Handler();
        delay += 250;
        handler.postDelayed(() -> client.addSchedule(schedules, registerScheduleRequest), delay);

        // This is extremely bad
        delay += DELAY;
        AtomicInteger id = new AtomicInteger();
        handler.postDelayed(() -> id.set(new ArrayList<>(schedules.keySet()).get(0)), delay);

        delay += DELAY;
        days.remove(0);
        days.add(Day.SATURDAY);
        days.add(Day.SUNDAY);
        handler.postDelayed(() -> {
            ChangeDaysScheduleRequest changeDaysScheduleRequest = new ChangeDaysScheduleRequest(id.get(), days);
            client.changeDaysSchedule(schedules, changeDaysScheduleRequest);
        }, delay);

        delay += DELAY;
        handler.postDelayed(() -> {
            ChangeTimeScheduleRequest changeTimeScheduleRequest = new ChangeTimeScheduleRequest(id.get(), "a");
            client.changeTimeSchedule(schedules, changeTimeScheduleRequest);
        }, delay);

        delay += DELAY;
        handler.postDelayed(() -> {
            ChangeGradientScheduleRequest changeGradientScheduleRequest = new ChangeGradientScheduleRequest(id.get(), 7216);
            client.changeGradientSchedule(schedules, changeGradientScheduleRequest);
        }, delay);

        delay += DELAY;
        handler.postDelayed(() -> {
            RenameScheduleRequest renameScheduleRequest = new RenameScheduleRequest(id.get(), "newName");
            client.renameSchedule(schedules, renameScheduleRequest);
        }, delay);

        delay += DELAY;
        handler.postDelayed(() -> client.activateSchedule(schedules, id.get()), delay);

        delay += DELAY;
        handler.postDelayed(() -> client.deactivateSchedule(schedules, id.get()), delay);

        delay += DELAY;
        handler.postDelayed(() -> client.deleteSchedule(schedules, id.get()), delay);
    }
}
