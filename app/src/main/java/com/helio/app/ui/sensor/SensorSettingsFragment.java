package com.helio.app.ui.sensor;

import android.os.Bundle;
import android.text.InputType;
import androidx.preference.EditTextPreference;
import androidx.preference.ListPreference;
import androidx.preference.Preference;
import androidx.preference.PreferenceFragmentCompat;
import com.helio.app.R;

public class SensorSettingsFragment extends PreferenceFragmentCompat {

    @Override
    public void onCreatePreferences(Bundle savedInstanceState, String rootKey) {
        setPreferencesFromResource(R.xml.sensor_preferences, rootKey);

        EditTextPreference namePreference = findPreference("name");
        EditTextPreference ipPreference = findPreference("ip");
        EditTextPreference inactivityDurationPreference = findPreference("inactivityDuration");
        ListPreference changeIconPreference = findPreference("changeIcon");
        ListPreference sensorTypePreference = findPreference("sensorType");


        assert ipPreference != null;
        ipPreference.setOnBindEditTextListener(editText -> editText.setInputType(InputType.TYPE_CLASS_PHONE));

        assert namePreference != null;
        namePreference.setOnBindEditTextListener(editText -> editText.setInputType(InputType.TYPE_CLASS_TEXT));

        assert  inactivityDurationPreference != null;
        inactivityDurationPreference.setOnBindEditTextListener(editText -> editText.setInputType(InputType.TYPE_CLASS_NUMBER));

        //When sensor type changes
        assert  sensorTypePreference != null;
        sensorTypePreference.setOnPreferenceChangeListener(new Preference.OnPreferenceChangeListener() {
            @Override
            public boolean onPreferenceChange(Preference preference, Object newValue) {
                if(newValue.toString().contains("Light")){
                    inactivityDurationPreference.setVisible(false);
                }else{
                    inactivityDurationPreference.setVisible(true);
                }
                return true;
            }
        });


    }
}