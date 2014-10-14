require "memoizable"

class Problem
	include Memoizable
	def find_routes(x, y)
		routes = 0
		if y > 0
			routes+=find_routes(x, y - 1)
		end
		if x > 0
			routes+=find_routes(x - 1, y)
		end
		if x == 0 && y == 0
			routes+=1
		end
		routes
	end
	memoize :find_routes
end

t = Time.now
p Problem.find_routes(20, 20)
t = Time.now - t
p "elapsed time: %.2f" % t