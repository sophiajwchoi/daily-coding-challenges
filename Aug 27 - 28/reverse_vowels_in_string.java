public class reverseVowelsOnly {

	public static void main(String[] args) {
		System.out.println(reverseVowel("Hello"));

	}
	
	public static String reverseVowel(String st) {
		int i = 0;
		int j = st.length() - 1;
		StringBuilder sbldr = new StringBuilder(st);
		
		while (i != j){
			if (!isVowel(sbldr.charAt(i))) {
				i++;
				continue;
			}
			if (!isVowel(sbldr.charAt(j))) {
				j--;
				continue;
			}

			char temp = sbldr.charAt(i);
			sbldr.setCharAt(i,st.charAt(j));
			sbldr.setCharAt(j,temp);
			i++;
			j--;

		}
		return sbldr.toString();
			
	}
	
	public static boolean isVowel(char c) {
		switch (c) {
			case 'A':
			case 'a':
			case 'E':
			case 'e':
			case 'I':
			case 'i':
			case 'O':
			case 'o':
			case 'U':
			case 'u':
				return true;
			default:
				return false;
		}
	}

}
