puts [2, 3, 4, 5, 10].
  sort.reverse.
  combination(3).
  each { |sides| l = sides.reduce(:+); break l if l > sides.max * 2 }