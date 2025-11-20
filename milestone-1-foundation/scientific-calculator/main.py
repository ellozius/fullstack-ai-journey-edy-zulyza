#!/usr/bin/env python3
"""
Scientific Calculator - CLI Entry Point
Milestone 1 Foundation - Fullstack AI Edy Zulyza
"""

import click
from src.calculators.basic_calculator import BasicCalculator
from src.calculators.scientific_calculator import ScientificCalculator

basic = BasicCalculator()
scientific = ScientificCalculator()

class OrderedGroup(click.Group):
    def list_commands(self, ctx):
        return [
            "add", "subtract", "multiply", "divide",
            "power", "sqrt", "factorial", "log",
            "sin", "cos", "tan",
            "radians", "degrees"
        ]

        
@click.group(cls=OrderedGroup)
def cli():
    """🧮 Scientific Calculator CLI - Milestone 1"""
    pass

# === Basic Operations ===
@cli.command()
@click.argument("a", type=float)
@click.argument("b", type=float)
def add(a, b):
    """Penjumlahan"""
    click.echo(f"Hasil: {basic.add(a, b)}")    
    
@cli.command()
@click.argument("a", type=float)
@click.argument("b", type=float)    
def subtract(a, b):
    """Pengurangan"""
    click.echo(f"Hasil: {basic.subtract(a, b)}")
    
@cli.command()
@click.argument("a", type=float)
@click.argument("b", type=float)
def multiply(a, b):
    """Perkalian"""
    click.echo(f"Hasil: {basic.multiply(a, b)}")
    
@cli.command()
@click.argument("a", type=float)
@click.argument("b", type=float)
def divide(a, b):
    """Pembagian"""
    try:
        click.echo(f"Hasil: {basic.divide(a, b)}")
    except ValueError as e:
        click.echo(f"Error: {e}")

# === Scientific Operations ===
@cli.command()
@click.argument("x", type=float)
def sqrt(x):
    """Akar kuadrat"""
    try:
        click.echo(f"Hasil: {scientific.sqrt(x)}")
    except ValueError as e:
        click.echo(f"Error: {e}")

@cli.command()
@click.argument("n", type=int)
def factorial(n):
    """Faktorial"""
    try:
        click.echo(f"Hasil: {scientific.factorial(n)}")
    except ValueError as e:
        click.echo(f"Error: {e}")
        
@cli.command()
@click.argument("base", type=float)
@click.argument("exponent", type=float)
def power(base, exponent):
    """Pangkat"""
    try:
        click.echo(f"Hasil: {scientific.power(base, exponent)}")
    except ValueError as e:
        click.echo(f"Error: {e}")

@cli.command()
@click.argument("degrees", type=float)
def radians(degrees):
    """Konversi derajat ke radian"""
    try:
        click.echo(f"Hasil: {scientific.radians(degrees)}")
    except ValueError as e:
        click.echo(f"Error: {e}")

@cli.command()
@click.argument("radians", type=float)
def degrees(radians):
    """Konversi radian ke derajat"""
    try:
        click.echo(f"Hasil: {scientific.degrees(radians)}")
    except ValueError as e:
        click.echo(f"Error: {e}")   
        
@cli.command()
@click.argument("value", type=float)
@click.option("--base", type=float, default=10, help="Basis logaritma (default: 10)") 
def log(value, base):
    """Logaritma (gunakan --base untuk basis (contoh : 5 --base 5 ), default: 10)"""
    try:
        click.echo(f"Hasil: {scientific.log(value, base)}")
    except ValueError as e:
        click.echo(f"Error: {e}")
        
@cli.command()
@click.argument("x", type=float)        
def sin(x):
    """Fungsi sinus (input dalam derajat)"""
    try:
        click.echo(f"Hasil: {scientific.sin(x)}")
    except ValueError as e:
        click.echo(f"Error: {e}")
        
@cli.command()
@click.argument("x", type=float)        
def cos(x):
    """Fungsi cosinus (input dalam derajat)"""
    try:
        click.echo(f"Hasil: {scientific.cos(x)}")
    except ValueError as e:
        click.echo(f"Error: {e}")   
        
@cli.command()
@click.argument("x", type=float)        
def tan(x):
    """Fungsi tangen (input dalam derajat)"""
    try:
        click.echo(f"Hasil: {scientific.tan(x)}")
    except ValueError as e:
        click.echo(f"Error: {e}")
        


if __name__ == "__main__":
    cli()