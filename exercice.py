#!/usr/bin/env python


def dissipated_power(voltage, resistance):
	P = (voltage**2)/resistance
	return P

def orthogonal(v1, v2):
	# TODO: Retourner vrai si les vecteurs sont orthogonaux, faux sinon.
	   #v1[0]  Pour accéder au X
	   #v1[1] # Pour accéder au Y
	if v1[0]*v2[0] + v1[1]*v2[0] == 0 or v1[0]+v1[1] == 0 or v2[0]+v2[1] == 0 :
		return True

	else:
		return False

def average(values):
	# TODO: Calculer la moyenne des valeurs positives (on ignore les valeurs strictement négatives).
	somme = 0
	v_1 = 0
	moyenne = 0
	for v in values:
	# La variable v contient une valeur de la liste.
		if v >= 0:
			somme += v
			v_1 += 1

		else:
			pass
	moyenne += (somme)/(v_1)

	return moyenne

def bills(value):
	# TODO: Calculez le nombre de billets de 20$, 10$ et 5$ et pièces de 1$ à remettre pour représenter la valeur.
	twenties = 0
	tens = 0
	fives = 0
	ones = 0
	while value != 0:
		if value >= 20:

			twenties += value//20
			value %= 20

		elif value >= 10:

			tens += value // 10
			value %= 10

		elif value >= 5:

			fives += value//5
			value %= 5

		elif value >= 1:

			ones += value
			value = 0

	return twenties, tens, fives, ones

def format_base(value, base, digit_letters):
	# Formater un nombre dans une base donné en utilisant les lettres fournies pour les chiffres<
	# `digits_letters[0]` Nous donne la lettre pour le chiffre 0, ainsi de suite.
	result = ""
	abs_value = abs(value)
	while abs_value != 0:
		digit_value = abs_value % base
		result += digit_letters[digit_value]
		abs_value //= base

	if value < 0:
		# TODO: Ne pas oublier d'ajouter '-' devant pour les nombres négatifs.
		result += "-"
	return result[::-1]


if __name__ == "__main__":
	print(dissipated_power(69, 420))
	print(orthogonal((1, 1), (-1, 1)))
	print(average([1, 4, -2, 10]))
	print(bills(137))
	print(format_base(7, 2, "0123456789ABCDEF"))
