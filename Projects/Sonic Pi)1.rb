use_synth :piano
in_thread do
  4.times do
    sleep 0.5
    play chord(:D4, :major)
    sleep 0.25
    play chord(:D4, :major7)
    sleep 0.5
    play chord(:A, :major)
    sleep 0.5
    play chord(:A, :major)
    sleep 0.5
    play chord(:G, :major)
    sleep 0.5
    play chord(:G, :major)
    sleep 0.5
    play chord(:E, :major)
    sleep 0.5
    2.times do
      use_bpm 90
      play chord(:F, :major)
      sleep 0.1
    end
    
  end
  sleep 1
  play :A5
end

in_thread do
  4.times do
    sleep 0.5
    play :G2, release: 0.35, amp: 0.6
    sleep 0.25
    play :A2, release: 0.35, amp: 0.6
    sleep 0.5
    play :G2, release: 0.35, amp: 0.6
    sleep 0.5
    play :A2, release: 0.35, amp: 0.6
    sleep 0.5
    play :G2, release: 0.35, amp: 0.6
    sleep 0.5
    play :A2, release: 0.35, amp: 0.6
    sleep 0.5
    play :G2, release: 0.35, amp: 0.6
    sleep 0.5
    2.times do
      use_bpm 90
      play :G2, amp: 0.35, release: 0.2
      sleep 0.1
    end
  end
  sleep 1
  sample :drum_cymbal_soft
end
in_thread do
  4.times do
    sleep 0.5
    sample :drum_heavy_kick
    sleep 0.25
    sample :drum_heavy_kick
    sleep 0.5
    sample :drum_heavy_kick
    sleep 0.5
    sample :drum_heavy_kick
    sleep 0.5
    sample :drum_heavy_kick
    sleep 0.5
    sample :drum_heavy_kick
    sleep 0.5
    sample :drum_heavy_kick
    sleep 0.5
    2.times do
      use_bpm 90
      sample :drum_heavy_kick
      sleep 0.1
    end
  end
  sleep 1
  play :D2
end
