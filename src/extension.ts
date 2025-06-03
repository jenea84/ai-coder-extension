import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
    // Просто регистрируем пустую панель
    const disposable = vscode.commands.registerCommand('ai-coder.test', () => {
        vscode.window.showInformationMessage('Панель работает!');
    });
    context.subscriptions.push(disposable);
}


export function deactivate() {}