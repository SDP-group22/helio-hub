package com.helio.app.ui.blind;

import android.graphics.Color;
import android.graphics.PorterDuff;
import android.graphics.drawable.Drawable;
import android.os.Bundle;
import android.text.InputType;
import android.widget.PopupWindow;

import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentTransaction;
import androidx.preference.EditTextPreference;
import androidx.preference.ListPreference;
import androidx.preference.Preference;
import androidx.preference.PreferenceFragmentCompat;

import com.helio.app.R;

public class SingleBlindSettingsPreferencesFragment extends PreferenceFragmentCompat {

    public static String blindName;

    @Override
    public void onCreatePreferences(Bundle savedInstanceState, String rootKey) {
        setPreferencesFromResource(R.xml.single_blind_preferences, rootKey);

        EditTextPreference namePreference = findPreference("name");
        EditTextPreference ipPreference = findPreference("ip");
        ListPreference changeIconPreference = findPreference("changeIcon");
        Preference calibrationPreference = findPreference("calibration");
        Preference openNowPreference = findPreference("openNow");
        Preference closeNowPreference = findPreference("closeNow");
        Preference createSchedulePreference = findPreference("createSchedule");
        Preference seeSchedulePreference = findPreference("seeSchedule");
        Preference sensor1Preference = findPreference("sensor1");
        Preference sensor2Preference = findPreference("sensor2");


        //IP
        assert ipPreference != null;
        ipPreference.setOnBindEditTextListener(editText -> editText.setInputType(InputType.TYPE_CLASS_PHONE));


        //Name
        assert namePreference != null;
        namePreference.setOnBindEditTextListener(editText -> editText.setInputType(InputType.TYPE_CLASS_TEXT));
        namePreference.setOnPreferenceChangeListener(new Preference.OnPreferenceChangeListener() {
            @Override
            public boolean onPreferenceChange(Preference preference, Object newValue) {
                blindName = String.valueOf(namePreference.getSummary());
                return true;
            }
        });




    }
}