# 99 Bottles on the wall

i = 19
while i -= 1
	s  = if i == 1   then "" else "s"
	s_ = if i-1 == 1 then "" else "s"
	console.log "#{i} bottle#{s} of beer on the wall, #{i} bottle#{s} of beer!\n
	Take one down, pass it around, #{i-1} bottle#{s_} of bear on the wall!"
