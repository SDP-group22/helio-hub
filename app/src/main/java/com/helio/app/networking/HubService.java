package com.helio.app.networking;

import com.helio.app.model.Day;
import com.helio.app.model.Motor;
import com.helio.app.model.Schedule;
import com.helio.app.networking.request.RegisterMotorRequest;
import com.helio.app.networking.request.RegisterScheduleRequest;

import java.util.List;

import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.DELETE;
import retrofit2.http.GET;
import retrofit2.http.PATCH;
import retrofit2.http.POST;
import retrofit2.http.Path;

/**
 * This interface matches the OpenAPI specification we came up with as a group.
 *
 * @see HubClient
 */
public interface HubService {
    @POST("/motor/register")
    Call<Motor> addMotor(@Body RegisterMotorRequest registerMotorRequest);

    @PATCH("/motor/activate/{motor_id}")
    Call<Motor> activateMotor(@Path("motor_id") int id);

    @PATCH("/motor/deactivate/{motor_id}")
    Call<Motor> deactivateMotor(@Path("motor_id") int id);

    @PATCH("/motor/rename/{motor_id}")
    Call<Motor> renameMotor(@Path("motor_id") int id, @Body String name);

    @GET("/motor/{motor_id}")
    Call<Motor> getMotor(@Path("motor_id") int id);

    @PATCH("/motor/move/{motor_id}")
    Call<Motor> moveMotor(@Path("motor_id") int id, @Body int level);

    @PATCH("/motor/start_calibrate/{motor_id}")
    Call<Motor> startMotorCalibration(@Path("motor_id") int id);

    @PATCH("/motor/stop_calibrate/{motor_id}")
    Call<Motor> stopMotorCalibration(@Path("motor_id") int id);

    @DELETE("/motor/unregister/{motor_id}")
    Call<ResponseBody> deleteMotor(@Path("motor_id") int id);

    @GET("/schedule/get_all")
    Call<List<Schedule>> getAllMotors();

    @POST("/schedule/register")
    Call<Schedule> addSchedule(@Body RegisterScheduleRequest registerScheduleRequest);

    @DELETE("/schedule/unregister/{schedule_id}")
    Call<ResponseBody> deleteSchedule(@Path("schedule_id") int id);

    @PATCH("/schedule/change_days/{schedule_id}")
    Call<Schedule> changeDaysSchedule(@Path("schedule_id") int id, @Body List<Day> days);

    @PATCH("/schedule/change_time/{schedule_id}")
    Call<Schedule> changeTimeSchedule(@Path("schedule_id") int id, @Body String time);

    @PATCH("/schedule/change_gradient/{schedule_id}")
    Call<Schedule> changeGradientSchedule(@Path("schedule_id") int id, @Body int gradient);

    @PATCH("/schedule/rename/{schedule_id}")
    Call<Schedule> renameSchedule(@Path("schedule_id") int id, @Body String name);

    @PATCH("/schedule/activate/{schedule_id}")
    Call<Schedule> activateSchedule(@Path("schedule_id") int id);

    @PATCH("/schedule/deactivate/{schedule_id}")
    Call<Schedule> deactivateSchedule(@Path("schedule_id") int id);
}
