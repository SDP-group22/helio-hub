package com.helio.app.ui.scheduling;

import android.app.TimePickerDialog;
import android.os.Bundle;
import android.os.Handler;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.TimePicker;

import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;
import androidx.lifecycle.ViewModelProvider;

import com.helio.app.R;

import java.util.Calendar;

public class ScheduleFragment extends Fragment {

    private ScheduleViewModel scheduleViewModel;

    private TextView openingHour;
    private TextView openingMinute;
    private TextView closingHour;
    private TextView closingMinute;
    private Button setOpeningTime;
    private Button cancelOpeningTime;
    private Button setClosingTime;
    private Button cancelClosingTime;
    private Button raise;
    private Button lower;
    private TimePickerDialog timePickerDialog;
    private Calendar calendar;
    private int currentHour;
    private int currentMinute;
    private int openingHourInt;
    private int openingMinuteInt;
    private int closingHourInt;
    private int closingMinuteInt;
    private Handler handler1;
    private Handler handler2;
    private Runnable runnable1;
    private Runnable runnable2;

//    //show toast for Raise
//    public void showToastRaise(View view){
//        Toast.makeText(this.getActivity(),"Raise Clicked!",Toast.LENGTH_LONG).show();
//    }
//
//    //show toast for lower
//    public void showToastLower(View view){
//        Toast.makeText(this.getActivity(),"Lower Clicked!",Toast.LENGTH_LONG).show();
//    }

    //time difference calculator
    public int timeDifference(int curHour, int curMinute, int curSecond, int destHour, int destMinute){
        int returnValue;
        if( (destHour > curHour) || (destHour == curHour && destMinute > curMinute )){
            returnValue = (destHour - curHour) * 60 * 60 + (destMinute - curMinute - 1) * 60 + (60 - curSecond);
            return returnValue;
        }else{
            returnValue = (destHour * 60 * 60 + destMinute * 60) + ((24 - curHour) * 60 * 60 + (0 - curMinute -1) * 60 + (60-curSecond));
            return returnValue;
        }
    }

    public View onCreateView(@NonNull LayoutInflater inflater,
                             ViewGroup container, Bundle savedInstanceState) {
        scheduleViewModel =
                new ViewModelProvider(this).get(ScheduleViewModel.class);
        View returnView = inflater.inflate(R.layout.fragment_schedule, container, false);

        //map variables to buttons
        openingHour = returnView.findViewById(R.id.tx_openingHour);
        openingMinute = returnView.findViewById(R.id.tx_openingMinute);
        setOpeningTime = returnView.findViewById(R.id.btn_setOpeningTime);
        cancelOpeningTime = returnView.findViewById(R.id.btn_cancelOpeningTime);
        closingHour = returnView.findViewById(R.id.tx_closingHour);
        closingMinute = returnView.findViewById(R.id.tx_closingMinute);
        setClosingTime = returnView.findViewById(R.id.btn_setClosingTime);
        cancelClosingTime = returnView.findViewById(R.id.btn_cancelClosingTime);
        raise = returnView.findViewById(R.id.btn_raise);
        lower = returnView.findViewById(R.id.btn_lower);



        //when click the opening "+"
        setOpeningTime.setOnClickListener((v) -> {
            calendar = Calendar.getInstance();
            currentHour = calendar.get(Calendar.HOUR_OF_DAY);
            currentMinute = calendar.get(Calendar.MINUTE);

            //show the timePickerDialog
            timePickerDialog = new TimePickerDialog(getActivity(), new TimePickerDialog.OnTimeSetListener() {
                @Override
                public void onTimeSet(TimePicker view, int hourOfDay, int minute) {
                    openingHourInt = hourOfDay;
                    openingMinuteInt = minute;
                    openingHour.setText(String.format("%02d",hourOfDay));
                    openingMinute.setText(String.format("%02d",minute));

                    //timer: when the time arrive, perform runnable1 (click "raise" and "-")
                    calendar = Calendar.getInstance();
                    int timeDiff = timeDifference(calendar.get(Calendar.HOUR_OF_DAY), calendar.get(Calendar.MINUTE), calendar.get(Calendar.SECOND), openingHourInt,openingMinuteInt);
                    handler1 = new Handler();
                    handler1.postDelayed(runnable1 = new Runnable() {
                        @Override
                        public void run() {
                            raise.performClick();
                            cancelOpeningTime.performClick();
                        }
                    }, timeDiff*1000);
                }
            }, currentHour,currentMinute,true);

            timePickerDialog.show();
        });

        //when click the opening "-"
        cancelOpeningTime.setOnClickListener((v)->{
            openingHourInt = -1;
            openingMinuteInt = -1;
            openingHour.setText("");
            openingMinute.setText("");
            handler1.removeCallbacks(runnable1);
        });

        //when click the closing "+"
        setClosingTime.setOnClickListener((v) -> {
            calendar = Calendar.getInstance();
            currentHour = calendar.get(Calendar.HOUR_OF_DAY);
            currentMinute = calendar.get(Calendar.MINUTE);

            //show the timePickerDialog
            timePickerDialog = new TimePickerDialog(getActivity(), new TimePickerDialog.OnTimeSetListener() {
                @Override
                public void onTimeSet(TimePicker view, int hourOfDay, int minute) {
                    closingHourInt = hourOfDay;
                    closingMinuteInt = minute;
                    closingHour.setText(String.format("%02d",hourOfDay));
                    closingMinute.setText(String.format("%02d",minute));

                    //timer: when the time arrive, perform runnable2 (click "lower" and "-")
                    calendar = Calendar.getInstance();
                    int timeDiff = timeDifference(calendar.get(Calendar.HOUR_OF_DAY), calendar.get(Calendar.MINUTE), calendar.get(Calendar.SECOND), closingHourInt,closingMinuteInt);
                    handler2 = new Handler();
                    handler2.postDelayed(runnable2 = new Runnable() {
                        @Override
                        public void run() {
                            lower.performClick();
                            cancelClosingTime.performClick();
                        }
                    }, timeDiff*1000);

                }
            }, currentHour,currentMinute,true);

            timePickerDialog.show();
        });

        //when click the closing "-"
        cancelClosingTime.setOnClickListener((v)->{
            closingHourInt = -1;
            closingMinuteInt = -1;
            closingHour.setText("");
            closingMinute.setText("");
            handler2.removeCallbacks(runnable2);

        });


        return returnView;
    }
}