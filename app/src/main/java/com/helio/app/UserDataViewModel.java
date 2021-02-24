package com.helio.app;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;

import com.helio.app.model.Motor;
import com.helio.app.networking.HubClient;

import java.util.Map;

public class UserDataViewModel extends ViewModel {
    private final HubClient client = new HubClient("http://10.0.2.2:4310/");
    private MutableLiveData<Map<Integer, Motor>> motors;
    private int currentMotorId = -1;

    public LiveData<Map<Integer, Motor>> fetchMotors() {
        if(motors == null) {
            motors = new MutableLiveData<>();
            client.getAllMotors(motors);
        }
        return motors;
    }

    public void setCurrentMotor(int id) {
        currentMotorId = id;
    }

    public void moveCurrentMotor(int level) {
        client.moveMotor(getCurrentMotor(), level);
    }

    public Motor getCurrentMotor() {
        return motors.getValue().get(currentMotorId);
    }
}
