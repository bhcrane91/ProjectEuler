class J19 {
	public static void main(String[] args) {

		//              Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
		int[] months = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
		// S 0 | M 1 | T 2 | W 3 | R 4 | F 5 | A 6
		int weekday = 0;
		int weekdayCount = 0; 
		int currWeekday = 1;

		for (int year = 1900; year <= 2000; year++) {
			if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) {
				months[1] = 29;
			}
			else {
				months[1] = 28;
			}

			for (int month: months) {
				currWeekday = (currWeekday + month) % 7;
				if (currWeekday == weekday && year > 1900) weekdayCount++;
			}
		}

		System.out.println(weekdayCount);
	}
}
