set_sched_ahead_time! 0
live_loop :listen do
  message = sync "/play_this"
  note = message[:args][0]
  play note
end
