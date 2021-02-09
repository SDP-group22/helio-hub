package com.helio.app.ui;

import android.os.Bundle;
import android.text.InputType;
import android.view.View;
import android.view.ViewGroup;
import android.widget.EditText;
import android.widget.PopupWindow;
import android.widget.Spinner;

import androidx.annotation.NonNull;
import androidx.preference.DropDownPreference;
import androidx.preference.EditTextPreference;
import androidx.preference.ListPreference;
import androidx.preference.Preference;
import androidx.preference.PreferenceFragmentCompat;
import androidx.preference.SwitchPreference;

import com.helio.app.R;

public class SettingsFragment extends PreferenceFragmentCompat {
    private PopupWindow changeIconPop;


    @Override
    public void onCreatePreferences(Bundle savedInstanceState, String rootKey) {
        setPreferencesFromResource(R.xml.preferences, rootKey);

        EditTextPreference namePreference = findPreference("name");
        EditTextPreference ipPreference = findPreference("ip");
        ListPreference changeIconPreference = findPreference("changeIcon");
        Preference calibrationPreference = findPreference("calibration");
        Preference openNowPreference = findPreference("openNow");
        Preference closeNowPreference = findPreference("closeNow");
        Preference createSchedulePreference = findPreference("createSchedule");
        Preference seeSchedulePreference = findPreference("seeSchedule");
        SwitchPreference sensorsPreference = findPreference("sensors");


        //IP
        ipPreference.setOnBindEditTextListener(new EditTextPreference.OnBindEditTextListener() {
            @Override
            public void onBindEditText(@NonNull EditText editText) {
                editText.setInputType(InputType.TYPE_CLASS_TEXT);
            }
        });


        //Name
        namePreference.setOnBindEditTextListener(new EditTextPreference.OnBindEditTextListener() {
            @Override
            public void onBindEditText(@NonNull EditText editText) {
                editText.setInputType(InputType.TYPE_CLASS_TEXT);
            }
        });

        //change icon








    }
}