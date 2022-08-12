class UsersController < CrudController
  before_action do
    set_klass(User)
    clean_password_fields(:user)
    set_user_type
  end

  def new
    super
    @resource.addresses.build
  end

  protected

  def collection
    super
    @resources = @resources.where(user_type: session[:user_type])
  end


  private

  def clean_password_fields(model)
    if params[:user] && params[:user][:password].blank?
      params[:user].delete(:password)
      params[:user].delete(:password_confirmation)
    end
  end

  def resource_params
    params.require(:user).permit(:email, :password, :password_confirmation,
                                 :user_type)
  end

  def set_user_type
    session[:user_type] = params[:user_type] if params[:user_type]
  end
end
