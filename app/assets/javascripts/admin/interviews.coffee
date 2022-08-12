$(document).ready ->
  $("#interview_same_employer").on 'switchChange.bootstrapSwitch', (event, state) ->
    other_employer = $('#interview_other_employer')
    if $(this).is ':checked'
      other_employer.val ''
      other_employer.attr 'disabled', true
    else
      other_employer.attr 'disabled', false
  $("#interview_same_employer").trigger 'switchChange.bootstrapSwitch'

  $(".working-fields-selector").on 'switchChange.bootstrapSwitch', (event, state) ->
    if $(this).is ':checked'
      $('.accident-fields').show()
    else
      $('.accident-fields').hide()
  $(".working-fields-selector").trigger 'switchChange.bootstrapSwitch'

  $("#interview_interview_working_time_attributes_worked_saturdays").on 'switchChange.bootstrapSwitch', (event, state) ->
    if $(this).is ':checked'
      $('#interview_interview_working_time_attributes_saturdays_started_at').attr('disabled', false)
      $('#interview_interview_working_time_attributes_saturdays_ended_at').attr('disabled', false)
    else
      $('#interview_interview_working_time_attributes_saturdays_started_at').attr('disabled', true)
      $('#interview_interview_working_time_attributes_saturdays_ended_at').attr('disabled', true)
  $("#interview_interview_working_time_attributes_worked_saturdays").trigger 'switchChange.bootstrapSwitch'
 
  $("#interview_interview_working_time_attributes_worked_sundays").on 'switchChange.bootstrapSwitch', (event, state) ->
    if $(this).is ':checked'
      $('#interview_interview_working_time_attributes_sundays_started_at').attr('disabled', false)
      $('#interview_interview_working_time_attributes_sundays_ended_at').attr('disabled', false)
    else
      $('#interview_interview_working_time_attributes_sundays_started_at').attr('disabled', true)
      $('#interview_interview_working_time_attributes_sundays_ended_at').attr('disabled', true)
  $("#interview_interview_working_time_attributes_worked_sundays").trigger 'switchChange.bootstrapSwitch'

  $("#interview_interview_working_time_attributes_worked_holidays").on 'switchChange.bootstrapSwitch', (event, state) ->
    if $(this).is ':checked'
      $('#interview_interview_working_time_attributes_holidays_started_at').attr('disabled', false)
      $('#interview_interview_working_time_attributes_holidays_ended_at').attr('disabled', false)
    else
      $('#interview_interview_working_time_attributes_holidays_started_at').attr('disabled', true)
      $('#interview_interview_working_time_attributes_holidays_ended_at').attr('disabled', true)
  $("#interview_interview_working_time_attributes_worked_holidays").trigger 'switchChange.bootstrapSwitch'

 
